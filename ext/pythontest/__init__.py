from docutils.parsers.rst import directives as docutildirectives
from . import directives, builder


def setup(app):
    for node in [directives.pythontest, directives.pythontestsave, directives.pythontestrestore]:
        app.add_node(node)

    app.add_builder(builder.Builder)
    app.connect('doctree-resolved', directives.remove_pythontest_nodes)

    docutildirectives.register_directive('pythontest', directives.PythonTest)
    docutildirectives.register_directive('code-block', directives.PTCodeBlock)
    docutildirectives.register_directive('sourcecode', directives.PTCodeBlock)
    docutildirectives.register_directive('code', directives.PTDocutilsCodeBlock)
