from docutils import nodes, writers
from sphinx.util.console import *
from . import translator
import sys
import builtins
import io


class FakeTurtle:
    def forward(self, *a): pass
    def right(self, *a): pass
    def left(self, *a): pass
    def circle(self, *a): pass
    def undo(self, *a): pass
    def begin_fill(self, *a): pass
    def end_fill(self, *a): pass
    def Turtle(self, *a): pass
    def Pen(self, *a): return self

sys.modules["turtle"] = FakeTurtle()


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
        elif "age" in prompt or "number" in prompt:
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
                            "help": lambda *a: None})
    static_ns = {"__builtins__": static_builtins}

    def __init__(self, builder):
        writers.Writer.__init__(self)
        self.builder = builder
        self.returncode = 0

    def print(self, *args, sep=" ", end="\n"):
        self.output += sep.join(map(str, args)) + end

    def translate(self):
        self.builder.info()
        visitor = translator.Translator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.fails = []
        over_tests = over_minor_fails = over_major_fails = 0
        self.output = ""

        for chapter, code_bits in visitor.result():
            self.print(chapter, "=" * len(chapter), sep="\n")
            tests = minor_fails = major_fails = 0
            for major, mode, code in code_bits:
                tests += 1
                if ">>>" in code:
                    succeeded, error, detail = self.test_interactive(code, mode)
                else:
                    succeeded, error, detail = self.test_static(code, mode)
                if not succeeded:
                    if major:
                        self.returncode = 1
                        self.fails.append((chapter, code, error, detail))
                        major_fails += 1

                        self.print(error + ":")
                        self.print("\n".join(["    " + i for i in code.split("\n")]))
                        self.print(detail)
                        self.print()
                    else:
                        minor_fails += 1
            self.print()
            self.print(tests, "code items")
            self.print(minor_fails, "minor fails")
            self.print(major_fails, "major fails")
            self.print()

            over_tests += tests
            over_minor_fails += minor_fails
            over_major_fails += major_fails

        for chapter, code, error, detail in self.fails:
            self.builder.info(red("In chapter ") + bold("'{}'".format(chapter)) + red(":"))
            self.builder.info("\n".join(["    " + i for i in code.split("\n")]))
            self.builder.info(red(error + ": ") + bold(detail))
            self.builder.info()

        self.builder.info(bold("{} code items".format(over_tests)))
        self.builder.info(yellow("{} minor fails".format(over_minor_fails)))
        self.builder.info(red("{} major fails".format(over_major_fails)))

        self.print("Overall", "=======", sep="\n")
        self.print(tests, "code items")
        self.print(minor_fails, "minor fails")
        self.print(major_fails, "major fails")
                
            
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

    def test_interactive(self, code, mode):
        section = output = ""
        parts = []
        for line in code.split("\n") + [">>> "]:
            if line.startswith(">>>"):
                if section:
                    parts.append((section, output.strip()))
                    section = output = ""
                section += line[4:] + "\n"
            elif line.startswith("... "):
                section += line[4:] + "\n"
            else:
                output += line + "\n"

        if not mode.compile:
            return self.passed

        for code, output in parts:
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
            res = res.strip()
            if res != output:
                return False, "Output failure", "'{}' (real) != '{}' (supposed)".format(res, output)

        return self.passed

    def test_static(self, code, mode):
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

    def set_returncode(self, app):
        app.statuscode = self.returncode
