from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives


class file_node(nodes.Element):
    pass


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


def file_role(typ, rawtext, text, lineno, inliner,
              options={}, content=[]):
    return [file_node(text=text, type=typ)], []


def setup(app):
    app.add_node(file_node, latex=(visit_file_latex, depart_file_latex))
    app.add_role("file", file_role)
    app.add_role("url", file_role)
