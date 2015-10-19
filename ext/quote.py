import docutils.nodes
from docutils.parsers.rst import Directive, directives


class quote_node(docutils.nodes.Element):
    pass


def visit_quote_latex(self, node):
    self.body.append("\\begin{chapquote}{" + node["author"] + "}\n")


def depart_quote_latex(self, node):
    self.body.append("\\end{chapquote}\n")


class Quote(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self):
        author = self.arguments[0].strip()
        node = quote_node(author=author)
        quote = self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(quote_node, latex=(visit_quote_latex, depart_quote_latex))
    app.add_directive("quote", Quote)
