from docutils import nodes, writers
from collections import defaultdict


class Translator(nodes.NodeVisitor):
    def __init__(self, document, builder):
        nodes.NodeVisitor.__init__(self, document)
        self.builder = builder
        self.sectionlevel = 0
        self.start = True
        self.pythontest = True
        self.chapters = []
        self.chapter = ""
        self.saved_pythontest_state = []
        self.code_bits = defaultdict(list)

    def result(self):
        for chapter in self.chapters:
            yield chapter, self.code_bits[chapter]

    def trace(self):
        #print("Pythontest current state:", "ON" if self.pythontest else "OFF")
        pass

    def visit_pythontest(self, node):
        self.pythontest = node["on"]
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
            self.code_bits[self.chapter].append((False, node.astext()))
        raise nodes.SkipNode

    def visit_literal_block(self, node):
        if self.pythontest:
            self.code_bits[self.chapter].append((True, node.astext()))
        raise nodes.SkipNode

    visit_doctest_block = visit_literal_block

    def visit_title(self, node):
        self.start = False
        if self.sectionlevel == 0 and isinstance(node.parent, nodes.section):
            self.chapter = node.astext()
            self.chapters.append(self.chapter)


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
