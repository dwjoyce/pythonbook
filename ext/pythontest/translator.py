from docutils import nodes, writers
from sphinx.util.console import *
from collections import defaultdict


class Mode:
    def __init__(self, compile, run, output):
        self.compile = compile
        self.run = run
        self.output = output

    def __bool__(self):
        return self.compile

    def __str__(self):
        return "<Mode compile={} run={} output={}>".format(self.compile, self.run, self.output)

    def __eq__(self, other):
        return self.compile == other.compile and self.run == other.run and self.output == other.output


MODES = {"off": Mode(False, False, False),
         "none": Mode(False, False, False),

         "compile": Mode(True, False, False),
         "norun": Mode(True, False, False),

         "run": Mode(True, True, False),
         "noexc": Mode(True, True, False),
         "nooutput": Mode(True, True, False),

         "on": Mode(True, True, True),
         "output": Mode(True, True, True),
         "all": Mode(True, True, True),
         }


class Translator(nodes.NodeVisitor):
    def __init__(self, document, builder):
        nodes.NodeVisitor.__init__(self, document)
        self.builder = builder
        self.sectionlevel = 0
        self.start = True
        self.pythontest = MODES["on"]
        self.chapters = []
        self.chapter = ""
        self.saved_pythontest_state = []
        self.code_bits = defaultdict(list)

    def result(self):
        for chapter in self.chapters:
            yield chapter, self.code_bits[chapter]

    def trace(self):
        #print("Pythontest current state:", self.pythontest)
        pass

    def visit_pythontest(self, node):
        self.pythontest = node["mode"]
        self.trace()
        raise nodes.SkipNode

    def visit_pythontestsave(self, node):
        self.saved_pythontest_state.append(self.pythontest)
        self.trace()
        raise nodes.SkipNode

    def visit_pythontestrestore(self, node):
        self.pythontest = self.saved_pythontest_state.pop()
        self.trace()
        raise nodes.SkipNode

    def visit_literal(self, node):
        if self.pythontest:
            self.code_bits[self.chapter].append((False, self.pythontest, node.astext()))
        raise nodes.SkipNode

    def visit_literal_block(self, node):
        if self.pythontest:
            self.code_bits[self.chapter].append((True, self.pythontest, node.astext()))
        raise nodes.SkipNode

    visit_doctest_block = visit_literal_block

    def visit_title(self, node):
        self.start = False
        if self.sectionlevel == 0 and isinstance(node.parent, nodes.section):
            self.chapter = node.astext()
            self.chapters.append(self.chapter)
            if self.pythontest != MODES["on"]:
                self.builder.info(yellow("Warning: pythontest mode on start of chapter {} is {}, not all".format(self.chapter, self.pythontest)))

    def visit_section(self, node):
        if not self.start:
            self.sectionlevel += 1

    def depart_section(self, node):
        self.sectionlevel = max(self.sectionlevel - 1, -1)

    visit_document = depart_section

    def unknown_visit(self, node):
        pass

    def unknown_departure(self, node):
        pass
