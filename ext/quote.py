import docutils.nodes
from docutils.parsers.rst import Directive, directives


class quote_node(docutils.nodes.Element):
    pass


def visit_quote_latex(self, node):
    author = node["author"]
    if node["source"]:
        author += r"\\\textit{\scriptsize " + node["source"] + "}"
    self.body.append("\\begin{chapquote}{" + author + "}\n")


def depart_quote_latex(self, node):
    self.body.append("\\end{chapquote}\n")


class Quote(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 2
    option_spec = {"source": directives.unchanged,
                   "author": directives.unchanged_required}
    final_argument_whitespace = True

    def run(self):
        node = quote_node(author=self.options.get("author", ""),
                          source=self.options.get("source", "").strip())
        quote = self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(quote_node, latex=(visit_quote_latex, depart_quote_latex))
    app.add_directive("quote", Quote)
