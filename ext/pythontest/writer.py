from docutils import nodes, writers
from sphinx.util.console import *
from . import translator


class Writer(writers.Writer):

    supported = ('sphinxlatex',)

    settings_defaults = {}

    output = None

    def __init__(self, builder):
        writers.Writer.__init__(self)
        self.builder = builder

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
            for major, code in code_bits:
                tests += 1
                if ">>>" in code:
                    succeeded, error, detail = self.test_interactive(code)
                else:
                    succeeded, error, detail = self.test_static(code)
                if not succeeded:
                    if major:
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

    def test_interactive(self, code):
        section = output = ""
        for line in code.split("\n") + [">>> "]:
            if line.startswith(">>> "):
                if section:
                    compiled, error, detail = self.compile(section, try_eval=True)
                    if not compiled:
                        return False, error, detail
                    section = output = ""
                section += line[4:] + "\n"
            elif line.startswith("... "):
                section += line[4:] + "\n"
            else:
                output += line + "\n"
        return True, "Passed", ""

    def test_static(self, code):
        compiled, error, detail = self.compile(code)
        if compiled:
            return True, "Passed", ""
        return False, error, detail
