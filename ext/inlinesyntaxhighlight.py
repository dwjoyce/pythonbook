# Modified from https://bitbucket.org/klorenz/sphinxcontrib-inlinesyntaxhighlight/raw/2140ab0285f0a48bb12b326b49da273d87cdc47f/sphinxcontrib/inlinesyntaxhighlight.py

from docutils.parsers.rst.roles import register_canonical_role, set_classes
from docutils.parsers.rst import directives
from docutils import nodes
import re

def code_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    r'''code_role override or create if older docutils used.

    This only creates a literal node without parsing the code. This will
    be done later in sphinx.  This override is not really needed, but it 
    might give some speed
    '''

    set_classes(options)

    language = options.get('language', '')
    classes = ['code']

    if 'classes' in options:
        classes.extend(options['classes'])

    if language and language not in classes:
        classes.append(language)

    node = nodes.literal(rawtext, text, classes=classes, language=language)
    
    #import rpdb2 ; rpdb2.start_embedded_debugger('foo')

    return [node], []

code_role.options = { 'class': directives.class_option,
                      'language': directives.unchanged }

register_canonical_role('code', code_role)


from sphinx.writers.latex import LaTeXTranslator


def visit_literal(self, node):
    if self.in_footnote:
        raise UnsupportedError('%s:%s: literal blocks in footnotes are '
                                'not supported by LaTeX' %
                                (self.curfilestack[-1], node.line))
    if self.in_title:
        return self.body.append(r'\texttt{')
    code = node.astext().rstrip().lstrip()
    lang = self.hlsettingstack[-1][0]
    linenos = code.count('\n') >= self.hlsettingstack[-1][1] - 1
    highlight_args = node.get('highlight_args', {})
    if 'language' in node:
        # code-block directives
        lang = node['language']
        highlight_args['force'] = True
    if 'linenos' in node:
        linenos = node['linenos']
    def warner(msg):
        self.builder.warn(msg, (self.curfilestack[-1], node.line))
    hlcode = self.highlighter.highlight_block(code, lang, warn=warner,
            linenos=linenos, **highlight_args)
    # workaround for Unicode issue
    hlcode = hlcode.replace('€', '@texteuro[]')
    hlcode = hlcode.replace(r'\begin{Verbatim}[commandchars=\\\{\}]',
                            '')
    hlcode = hlcode.replace('\\end{Verbatim}',
                            '')
    self.body.append(r'\code{' + hlcode.rstrip().lstrip() + '}')
    raise nodes.SkipNode

def depart_literal(self, node):
    self.no_contractions -= 1
    self.body.append('}')


import types


LaTeXTranslator.visit_literal  = visit_literal
LaTeXTranslator.depart_literal = depart_literal


def setup(app):
    app.add_config_value('inline_highlight_literals', True, 'env')
    app.add_config_value('inline_highlight_respect_highlight', True, 'env')

    # add option if ``...`` (literal without node.role attribute, shall be highlighted)