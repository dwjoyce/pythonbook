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


import sphinx.writers.latex

class ISLLaTeXTranslator(sphinx.writers.latex.LaTeXTranslator):
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
        if self.table:
            self.body.append(hlcode.rstrip().lstrip())
        else:
            self.body.append(r'\code{' + hlcode.rstrip().lstrip() + '}')
        raise nodes.SkipNode

    def depart_literal(self, node):
        self.no_contractions -= 1
        self.body.append('}')


    def visit_literal_block(self, node):
        if self.in_footnote:
            raise UnsupportedError('%s:%s: literal blocks in footnotes are '
                                    'not supported by LaTeX' %
                                    (self.curfilestack[-1], node.line))
        if node.rawsource != node.astext():
            # most probably a parsed-literal block -- don't highlight
            self.body.append('\\begin{alltt}\n')
        else:
            code = node.astext().rstrip('\n')
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
            # must use original Verbatim environment and "tabular" environment
            viac = "\\def\FrameCommand{\\mycolorbox}\n\\setlength\\verbatimindentadjustcoefficient{40pt}\n"
            if self.table:
                self.table.has_problematic = True
                viac = "\\def\FrameCommand{\\mycolorboxdecol}\n\\setlength\\verbatimindentadjustcoefficient{0pt}\n"
                #self.table.has_verbatim = True
            # get consistent trailer
            hlcode = hlcode.rstrip() + '\n'

            #self.body.append('\n\\begin{adjustwidth}{1em}{0pt}\n' + hlcode + '\\end{adjustwidth}\n')
            self.body.append('\n' + viac + hlcode)
            raise nodes.SkipNode


    def depart_table(self, node):
        self.table.has_problematic = True
        if self.table.rowcount > 30:
            self.table.longtable = True
        self.body = self._body
        if not self.table.longtable and self.table.caption is not None:
            self.body.append('\n\n\\begin{threeparttable}\n'
                                '\\capstart\\caption{%s}\n' % self.table.caption)
        if self.table.longtable:
            self.body.append('\n\\begin{longtable}')
            endmacro = '\\end{longtable}\n\n'
        elif self.table.has_verbatim:
            self.body.append('\n\\begin{tabular}')
            endmacro = '\\end{tabular}\n\n'
        elif self.table.has_problematic and not self.table.colspec:
            # if the user has given us tabularcolumns, accept them and use
            # tabulary nevertheless
            self.body.append('\n\\begin{tabular}')
            endmacro = '\\end{tabular}\n\n'
        else:
            self.body.append('\n\\begin{tabulary}{\\linewidth}')
            endmacro = '\\end{tabulary}\n\n'
        if self.table.colspec:
            self.body.append(self.table.colspec)
        else:
            if self.table.has_problematic:
                colwidth = 0.95 / self.table.colcount
                colspec = ('p{%.3f\\linewidth}|' % colwidth) * \
                            self.table.colcount
                self.body.append('{|' + colspec + '}\n')
            elif self.table.longtable:
                self.body.append('{|' + ('l|' * self.table.colcount) + '}\n')
            else:
                self.body.append('{|' + ('L|' * self.table.colcount) + '}\n')
        if self.table.longtable and self.table.caption is not None:
            self.body.append('\\caption{%s} \\\\\n' % self.table.caption)
        if self.table.caption is not None:
            for id in self.next_table_ids:
                self.body.append(self.hypertarget(id, anchor=False))
            self.next_table_ids.clear()
        if self.table.longtable:
            self.body.append('\\hline\n')
            if len(self.tableheaders) > 1:
                self._body.append('\\rowcolor{TableHeaderColor}\n')
            self.body.extend(self.tableheaders)
            self.body.append('\\endfirsthead\n\n')
            self.body.append('\\multicolumn{%s}{c}%%\n' % self.table.colcount)
            self.body.append(r'{{\textsf{\tablename\ \thetable{} -- %s}}} \\'
                                % _('continued from previous page'))
            self.body.append('\n\\hline\n')
            self.body.extend(self.tableheaders)
            self.body.append('\\endhead\n\n')
            self.body.append(r'\hline \multicolumn{%s}{|r|}{{\textsf{%s}}} \\ \hline'
                                % (self.table.colcount,
                                _('Continued on next page')))
            self.body.append('\n\\endfoot\n\n')
            self.body.append('\\endlastfoot\n\n')
        else:
            self.body.append('\\hline\n')
            if len(self.tableheaders) > 1:
                self._body.append('\\rowcolor{TableHeaderColor}\n')
            self.body.extend(self.tableheaders)
        self.body.extend(self.tablebody)
        self.body.append(endmacro)
        if not self.table.longtable and self.table.caption is not None:
            self.body.append('\\end{threeparttable}\n\n')
        self.table = None
        self.tablebody = None

    def visit_thead(self, node):
        self.table.had_head = True
        if self.next_table_colspec:
            self.table.colspec = '{%s}\n' % self.next_table_colspec
        self.next_table_colspec = None
        # Redirect head output until header is finished. see visit_tbody.
        self.body = self.tableheaders


def setup(app):
    app.add_config_value('inline_highlight_literals', True, 'env')
    app.add_config_value('inline_highlight_respect_highlight', True, 'env')
    sphinx.writers.latex.LaTeXTranslator = ISLLaTeXTranslator
