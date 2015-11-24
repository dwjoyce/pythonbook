from docutils import nodes, writers
from sphinx.util.console import *
from . import translator
import sys
import builtins
import io
from code import compile_command
import keyword
import tokenize
import pep8
import re


class FakeTurtle:
    def forward(self, *a): pass
    def right(self, *a): pass
    def left(self, *a): pass
    def up(self, *a): pass
    def down(self, *a): pass
    def circle(self, *a): pass
    def undo(self, *a): pass
    def begin_fill(self, *a): pass
    def end_fill(self, *a): pass
    def fillcolor(self, *a): pass
    def Turtle(self, *a): pass
    def Pen(self, *a): return self
    def speed(self, *a): pass
    def pencolor(self, *a): pass
    def pensize(self, *a): pass
    def window_width(self, *a): return 100
    def window_height(self, *a): return 100
    def goto(self, *a): pass

sys.modules["turtle"] = FakeTurtle()


class FakeFile(list):
    def __init__(self, *a): pass
    def write(self, *a): pass
    def writelines(self, *a): pass
    def read(self, *a): return ""
    def readlines(self, *a): return []
    def close(self, *a): pass
    def seek(self, *a): pass


operators = "+ - / * ** = == != /= += -= **= ( ) { } // //= [ ] , : ; ' \" \\' \\\" < > <= >= ^ ~ & | << >> and or in . \\n \\t % %= *=".split() + ["is not"]
word_re = re.compile("(({})\w*)*".format("|".join(map(re.escape, operators))))


class Writer(writers.Writer):
    supported = ('sphinxlatex',)
    settings_defaults = {}
    output = None
    passed = True, "Passed", ""
    stdout = io.StringIO()
    static_builtins = builtins.__dict__.copy()

    def input(prompt=""):
        prompt = prompt.strip().lower()
        if "stop" in prompt:
            return "stop"
        elif "age" in prompt or "num" in prompt:
            return "10"
        elif "name" in prompt:
            return "quit"
        return ""

    def pre_test(self):
        self.stdout = io.StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.stdout

    def post_test(self):
        sys.stdout = self.old_stdout

    static_builtins.update({"input": input,
                            "open": FakeFile,
                            "help": lambda *a: None})
    static_ns = {"__builtins__": static_builtins,
                 "string": __import__("string")}

    def __init__(self, builder, app):
        writers.Writer.__init__(self)
        self.builder = builder
        self.returncode = 0
        self.fails = []
        self.pep8 = []
        self.app = app

    def print(self, *args, sep=" ", end="\n"):
        self.output += sep.join(map(str, args)) + end

    def write(self, doctree, dest):
        self.dest = dest.destination_path
        super().write(doctree, dest)

    def translate(self):
        self.builder.info()
        visitor = translator.Translator(self.document, self.builder)
        self.document.walkabout(visitor)
        over_tests = over_minor_fails = over_major_fails = 0
        self.warnings = warnings = visitor.warnings
        self.fails.extend(visitor.errors)
        over_minor_fails += sum(not x for x, *_ in visitor.errors)
        over_major_fails += sum(x for x, *_ in visitor.errors)
        self.output = ""

        for chapter, code_bits in visitor.result():
            self.print(chapter, "=" * len(chapter), sep="\n")
            tests = minor_fails = major_fails = 0
            for major, mode, code in code_bits:
                tests += 1
                if ">>>" in code:
                    succeeded, error, detail = self.test_interactive(code, mode,
                                                                     warnings, chapter if major else None)
                else:
                    succeeded, error, detail = self.test_static(code, mode,
                                                                warnings, chapter if major else None)
                if not succeeded:
                    if major:
                        self.fails.append((True, chapter, code, error, detail))
                        major_fails += 1

                        self.print(error + ":")
                        self.print("\n".join(["    " + i for i in code.split("\n")]))
                        self.print(detail)
                        self.print()
                    else:
                        if not self.minor_retest(code, mode):
                            self.fails.append((False, chapter, code, error, detail))
                            self.print(error + ":")
                            self.print("\n".join(["    " + i for i in code.split("\n")]))
                            self.print(detail)
                            self.print()
                            minor_fails += 1
            self.print()
            self.print(tests, "code items")
            self.print(minor_fails, "minor fails")
            self.print(major_fails, "major fails")
            self.print()

            over_tests += tests
            over_minor_fails += minor_fails
            over_major_fails += major_fails

        self.complete_pep8()

        for major, chapter, code, error, detail in self.fails:
            if major:
                self.builder.info(red("In chapter ") + bold("'{}'".format(chapter)) + red(":"))
                self.builder.info("\n".join(["    " + i for i in code.split("\n")]))
                self.builder.info(red(error + ": ") + bold(detail))
                self.builder.info()
            else:
                self.builder.info(yellow("Minor fail in chapter ") + bold("'{}'".format(chapter)) + yellow(": ") + bold(code))
                self.builder.info()

        for chapter, code, error, detail in warnings:
            self.builder.info(yellow("In chapter ") + bold("'{}'".format(chapter)) + yellow(":"))
            self.builder.info("\n".join(["    " + i for i in code.split("\n")]))
            self.builder.info(yellow(error + ": ") + bold(detail))
            self.builder.info()

        self.builder.info(bold("{} code items".format(over_tests)))
        self.builder.info(yellow("{} warnings".format(len(warnings))))
        self.builder.info(yellow("{} minor fails".format(over_minor_fails)))
        self.builder.info(red("{} major fails".format(over_major_fails)))
        self.builder.info(red("{} sphinx errors / warnings".format(self.app._warncount)))

        self.print("Overall", "=======", sep="\n")
        self.print(tests, "code items")
        self.print(over_minor_fails, "minor fails")
        self.print(over_major_fails, "major fails")
        self.print(self.app._warncount, "sphinx errors / warnings")
        self.app.statuscode += over_major_fails + self.app._warncount

    def compile(self, code, try_eval=False):
        if try_eval:
            try:
                return True, None, compile(code, "", "eval")
            except:
                pass
        try:
            return True, None, compile(code, "", "exec")
        except BaseException as e:
            return False, "Compilation failure", "{} - {}".format(type(e).__name__, str(e))

    def test_interactive(self, code, mode, warnings, chapter):
        section = output = ""
        parts = []
        orig_code = code
        code = code.split("\n")
        while code:
            line = code.pop(0)
            if line.startswith(">>>"):
                if section:
                    parts.append((section, output.strip()))
                    section = output = ""
                section += line[4:] + "\n"
                try:
                    cc = compile_command(section)
                except Exception as e:
                    return False, "Compilation failure", "{} - {}".format(type(e).__name__, str(e))
                else:
                    if cc is None:
                        while code:
                            if code[0].strip().startswith(">>>"):
                                break
                            line = code.pop(0)
                            if not line.strip():
                                break
                            if not line.startswith("    "):
                                break
                            section += line[4:] + "\n"
            else:
                output += line + "\n"
        if section:
            parts.append((section, output.strip()))

        if not mode.compile:
            return self.passed

        for code, output in parts:
            if chapter and code.strip():
                self.pep8.append((chapter, code))
            compiled, error, detail = self.compile(code, try_eval=True)
            if not compiled:
                return False, error, detail

            if not mode.run:
                continue
            self.pre_test()
            try:
                res = eval(detail, self.static_ns, self.static_ns)
            except BaseException as e:
                self.post_test()
                return False, "Execution failure", "{} - {}".format(type(e).__name__, str(e))
            self.post_test()

            if not mode.output:
                continue
            if res is None:
                res = ""
            else:
                res = repr(res)
            res = self.stdout.getvalue() + res
            res = "\n".join(map(str.rstrip, res.split("\n"))).strip()
            if res != output:
                return False, "Output failure", "'{}' (real) != '{}' (supposed)".format(res, output)

        return self.passed

    def test_static(self, code, mode, warnings, chapter):
        if chapter and code.strip():
            self.pep8.append((chapter, code))
        if not mode.compile:
            return self.passed

        compiled, error, detail = self.compile(code)
        if not compiled:
            return False, error, detail

        if not mode.run:
            return self.passed
        self.pre_test()
        try:
            exec(detail, self.static_ns, self.static_ns)
        except BaseException as e:
            self.post_test()
            return False, "Execution failure", "{} - {}".format(type(e).__name__, str(e))
        self.post_test()
        return self.passed

    def minor_retest(self, code, mode):
        if keyword.iskeyword(code):
            return True
        if code in operators:
            return True
        if word_re.match(code):
            return True
        #try:
            #list(tokenize.generate_tokens(io.StringIO(code).readline))
        #except Exception as e:
            #if "EOF in multi-line statement" in str(e):
                #return True
        #else:
            #return True
        return False

    def complete_pep8(self):
        fname = self.dest.rsplit(".", 1)[0] + "{}.py"
        for i, (chapter, code) in enumerate(self.pep8):
            with open(fname.format(i), "w") as f:
                f.write(code.rstrip("\n") + "\n")
        msgs = []
        pep8.print = lambda m, **_: msgs.append(m)
        checker = pep8.StyleGuide(paths=[fname.format(i) for i in range(len(self.pep8))])
        report = checker.check_files()
        r = re.compile(re.escape(self.dest.rsplit(".", 1)[0]) + "(\d+)\.py:(\d+):\d+: (\w*) (.*)$")
        for i in [fname.format(i) for i in range(len(self.pep8))]:
            os.remove(i)
        for filenum, line, code, msg in [r.match(i).groups() for i in msgs]:
            if code in ["E501"]:
                continue
            self.warnings.append(self.pep8[int(filenum)] + ("PEP8 fail", "{} - {}".format(code, msg)))
