from docutils import nodes
from docutils.parsers.rst import Directive, directives

from sphinx import addnodes
from sphinx.util import parselinenos
from sphinx.util.nodes import set_source_info
from sphinx.directives import CodeBlock

from . import builder
from .translator import MODES


class pythontest(nodes.Element):
    pass

class pythontestsave(nodes.Element):
    pass

class pythontestrestore(nodes.Element):
    pass


class PythonTest(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        mode = self.arguments[0].strip().lower()
        return [pythontest(mode=MODES[mode])]

class PTCodeBlock(CodeBlock):
    """
    Directive for a code block with special highlighting or line numbering
    settings.
    """

    has_content = CodeBlock.has_content
    required_arguments = CodeBlock.required_arguments
    optional_arguments = CodeBlock.optional_arguments
    final_argument_whitespace = CodeBlock.final_argument_whitespace
    option_spec = CodeBlock.option_spec
    option_spec.update({'pythontest': directives.unchanged})

    def run(self):
        literal, = super().run()
        if 'pythontest' in self.options:
            mode = self.options['pythontest'].strip().lower()
            return [pythontestsave(), pythontest(mode=MODES[mode]), literal, pythontestrestore()]
        return [literal]

class PTDocutilsCodeBlock(directives.body.CodeBlock):
    """
    Directive for a code block with special highlighting or line numbering
    settings.
    """

    has_content = directives.body.CodeBlock.has_content
    required_arguments = directives.body.CodeBlock.required_arguments
    optional_arguments = directives.body.CodeBlock.optional_arguments
    final_argument_whitespace = directives.body.CodeBlock.final_argument_whitespace
    option_spec = directives.body.CodeBlock.option_spec
    option_spec.update({'pythontest': directives.unchanged})

    def run(self):
        literal, = super().run()
        if 'pythontest' in self.options:
            mode = self.options['pythontest'].strip().lower()
            return [pythontestsave(), pythontest(mode=MODES[mode]), literal, pythontestrestore()]
        return [literal]


def remove_pythontest_nodes(app, doctree, fromdocname):
    if isinstance(app.builder, builder.Builder):
        return

    app.info("removing pythontest... " + fromdocname)
    for nodetype in [pythontest, pythontestsave, pythontestrestore]:
        for node in doctree.traverse(nodetype):
            node.replace_self([])
