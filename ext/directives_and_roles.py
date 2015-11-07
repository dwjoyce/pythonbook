from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives
import itertools
import re


class quote_node(nodes.Element):
    pass


class file_node(nodes.Element):
    pass


class framed_node(nodes.Element):
    pass


class raw_latex_node(nodes.Element):
    pass


def visit_quote_latex(self, node):
    author = node["author"]
    if node["source"]:
        author += r"\\\textit{\scriptsize " + node["source"] + "}"
    self.body.append("\\begin{chapquote}{" + author + "}\n")


def depart_quote_latex(self, node):
    self.body.append("\\end{chapquote}\n")
    next_node = node.parent[node.parent.index(node) + 1]
    if isinstance(next_node, nodes.section) and len(next_node[0].astext()) < 20:
        self.body.append(r"\vspace{-9mm}")


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


def visit_file_latex(self, node):
    if node["type"] == "file":
        t = r"\texttt{\small\color{OuterLinkColor}" + self.encode_uri(node["text"]) + "}"
    elif node["type"] == "url":
        t = r"{\small \url{" + self.encode_uri(node["text"]) + "}}"
    if self.in_title:
        t = t.replace(r"\small", "")
    self.body.append(t)
    raise nodes.SkipNode


def depart_file_latex(self, node):
    pass


def visit_framed_latex(self, node):
    a = node["border"] if "border" in node else "VerbatimBorderColor"
    b = node["background"] if "background" in node else "VerbatimColor"
    c = node["foreground"] if "foreground" in node else "VerbatimTextColor"
    self.body.append(r"\framedtext{" + a + "}{" + b + "}{" + c + "}{")
    if "code" in node and node["code"]:
        self.body.append(r"\small\texttt{")


def depart_framed_latex(self, node):
    if "code" in node and node["code"]:
        self.body.append(r"}")
    self.body.append("}")


def visit_raw_latex(self, node):
    self.body.append(node["latex"])
    raise nodes.SkipNode


def depart_raw_latex(self, node):
    pass


def file_role(typ, rawtext, text, lineno, inliner,
              options={}, content=[]):
    return [file_node(text=text, type=typ)], []


kbd_re = re.compile("(-)")


def kbd_role(typ, rawtext, text, lineno, inliner,
             options={}, content=[]):
    node = framed_node(code=True, background="white", border="black")
    for i, t in zip(kbd_re.split(text), itertools.cycle([nodes.strong, nodes.Text])):
        node += t(i, i)
    return [node], []


menu_re = re.compile("(->)")


def menu_role(typ, rawtext, text, lineno, inliner,
              options={}, content=[]):
    node = framed_node(code=True, background="white", border="black")
    for i, j in zip(menu_re.split(text), itertools.cycle(range(2))):
        if not j:
            node += nodes.strong(i.strip(), i.strip())
        else:
            node += raw_latex_node(latex=r"$\quad\longrightarrow\quad$")
    return [node], []


def setup(app):
    app.add_node(quote_node, latex=(visit_quote_latex, depart_quote_latex))
    app.add_directive("quote", Quote)

    app.add_node(file_node, latex=(visit_file_latex, depart_file_latex))
    app.add_role("file", file_role)
    app.add_role("url", file_role)

    app.add_node(framed_node, latex=(visit_framed_latex, depart_framed_latex))
    app.add_node(raw_latex_node, latex=(visit_raw_latex, depart_raw_latex))
    app.add_role("kbd", kbd_role)
    app.add_role("menu", menu_role)
    app.add_role("button", menu_role)
