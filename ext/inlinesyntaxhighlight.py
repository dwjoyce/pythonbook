# Modified from https://bitbucket.org/klorenz/sphinxcontrib-inlinesyntaxhighlight/raw/2140ab0285f0a48bb12b326b49da273d87cdc47f/sphinxcontrib/inlinesyntaxhighlight.py

from docutils.parsers.rst.roles import register_canonical_role, set_classes
from docutils.parsers.rst import directives
from docutils import nodes
import re
import shlex
import sphinx.writers.latex
from sphinx import addnodes
from sphinx.util import nodes as sphinxnodes


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


class ISLLaTeXTranslator(sphinx.writers.latex.LaTeXTranslator):
    def __init__(self, *args):
        super().__init__(*args)
        self.definition = 0

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
            self.body.append(r'\noframecode{' + hlcode.rstrip().lstrip() + '}')
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
            coeff = 40# if self.definition else 40
            verbatim_mode = ""
            viac = "\\setlength\\verbatimindentadjustcoefficient{" + str(coeff) + "pt}\n"
            if self.table:
                verbatim_mode = "framed"
                self.table.has_problematic = True
                viac = "\\setlength\\verbatimindentadjustcoefficient{0pt}\n"
                #self.table.has_verbatim = True
            # get consistent trailer
            hlcode = hlcode.rstrip() + '\n'
            hlcode = hlcode.replace(r'\begin{Verbatim}[commandchars=\\\{\}]' + "\n",
                                    r'')
            hlcode = hlcode.replace('\\end{Verbatim}\n',
                                    '')
            hlcode = hlcode.replace(' ',
                                    '\\hspace{\\charwidth}')
            hlcode = hlcode.strip("\n").replace('\n',
                                                '~\\breaktext{{\PYG{c}{Cont...}}}{}\n')
            self.body.append('\n' + viac + r"\non" + verbatim_mode + "verbatim{" + hlcode + r"}")
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
                colspec = ('m{%.3f\\linewidth}|' % colwidth) * \
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
            if self.tableheaders:
                self._body.append('\\rowcolor{TableHeaderColor}\n')
            self.body.extend([("\\textbf{" + i + "}") if "textsf" in i else i for i in self.tableheaders])
            self.body.append('\\endfirsthead\n\n')
            self.body.append('\\multicolumn{%s}{c}%%\n' % self.table.colcount)
            self.body.append(r'{} \\')
            self.body.append('\n\\hline\n')
            #self.body.extend(self.tableheaders)
            self.body.append('\\endhead\n')
            self.body.append(r'\hline\rowcolor{TableHeaderColor} \multicolumn{%s}{|r|}{{\textsf{\textit{%s}}}} \\ \hline'
                                % (self.table.colcount,
                                'Continued on next page'))
            self.body.append('\n\\endfoot\n\n')
            self.body.append('\\endlastfoot\n\n')
        else:
            self.body.append('\\hline\n')
            if self.tableheaders:
                self._body.append('\\rowcolor{TableHeaderColor}\n')
            self.body.extend([("\\textbf{" + i + "}") if "textsf" in i else i for i in self.tableheaders])
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

    def visit_image(self, node):
        attrs = node.attributes
        pre = []                        # in reverse order
        post = []
        include_graphics_options = []
        is_inline = self.is_inline(node)
        if 'scale' in attrs:
            # Could also be done with ``scale`` option to
            # ``\includegraphics``; doing it this way for consistency.
            pre.append('\\scalebox{%f}{' % (attrs['scale'] / 100.0,))
            post.append('}')
        if 'width' in attrs:
            w = self.latex_image_length(attrs['width'])
            if w:
                include_graphics_options.append('width=%s' % w)
        if 'height' in attrs:
            h = self.latex_image_length(attrs['height'])
            if h:
                include_graphics_options.append('height=%s' % h)
        if 'align' in attrs:
            align_prepost = {
                # By default latex aligns the top of an image.
                (1, 'top'): ('{\\hspace*{\\fill}', '\\hspace*{\\fill}}'),
                (1, 'middle'): ('{\\hspace*{\\fill}\\raisebox{-0.5\\height}{', '}\\hspace*{\\fill}}'),
                (1, 'bottom'): ('{\\hspace*{\\fill}\\raisebox{-\\height}{', '}\\hspace*{\\fill}}'),
                (0, 'center'): ('{\\hfill', '\\hfill}'),
                # These 2 don't exactly do the right thing.  The image should
                # be floated alongside the paragraph.  See
                # http://www.w3.org/TR/html4/struct/objects.html#adef-align-IMG
                (0, 'left'): ('{', '\\hfill}'),
                (0, 'right'): ('{\\hfill', '}'),}
            try:
                pre.append(align_prepost[is_inline, attrs['align']][0])
                post.append(align_prepost[is_inline, attrs['align']][1])
            except KeyError:
                pass
        if not is_inline:
            pre.append('\n')
            post.append('\n')
        pre.reverse()
        if node['uri'] in self.builder.images:
            uri = self.builder.images[node['uri']]
        else:
            # missing image!
            if self.ignore_missing_images:
                return
            uri = node['uri']
        if uri.find('://') != -1:
            # ignore remote images
            return
        self.body.extend(pre)
        options = ''
        if include_graphics_options:
            options = '[%s]' % ','.join(include_graphics_options)
        self.body.append('\\includegraphics%s{%s}' % (options, uri))
        self.body.extend(post)

    def visit_definition_list(self, node):
        self.definition += 1
        super().visit_definition_list(node)

    def depart_definition_list(self, node):
        super().depart_definition_list(node)
        self.definition -= 1

    def visit_term(self, node):
        ctx = '}] \\leavevmode'
        if node.get('ids'):
            ctx += "".join(self.hypertarget(i) for i in node['ids'])
        self.body.append('\\item[{')
        self.context.append(ctx)

    def visit_definition(self, node):
        self.body.append("\n")

    def visit_title(self, node):
        parent = node.parent
        if isinstance(parent, addnodes.seealso):
            # the environment already handles this
            raise nodes.SkipNode
        elif self.this_is_the_title:
            if len(node.children) != 1 and not isinstance(node.children[0],
                                                          nodes.Text):
                self.builder.warn('document title is not a single Text node',
                                  (self.curfilestack[-1], node.line))
            if not self.elements['title']:
                # text needs to be escaped since it is inserted into
                # the output literally
                self.elements['title'] = node.astext().translate(tex_escape_map)
            self.this_is_the_title = 0
            raise nodes.SkipNode
        elif isinstance(parent, nodes.section):
            try:
                self.body.append(r'\%s{{' % self.sectionnames[self.sectionlevel])
            except IndexError:
                # just use "subparagraph", it's not numbered anyway
                self.body.append(r'\%s{{' % self.sectionnames[-1])
            self.context.append('}}\n')

            if self.next_section_ids:
                for id in self.next_section_ids:
                    self.context[-1] += self.hypertarget(id, anchor=False)
                self.next_section_ids.clear()

        elif isinstance(parent, (nodes.topic, nodes.sidebar)):
            self.body.append(r'\textbf{')
            self.context.append('}}\n\n\medskip\n\n')
        elif isinstance(parent, nodes.Admonition):
            self.body.append('{')
            self.context.append('}}\n')
        elif isinstance(parent, nodes.table):
            self.table.caption = self.encode(node.astext())
            raise nodes.SkipNode
        else:
            self.builder.warn(
                'encountered title node not in section, topic, table, '
                'admonition or sidebar',
                (self.curfilestack[-1], node.line or ''))
            self.body.append('\\textbf{')
            self.context.append('}}\n')
        self.in_title = 1

aliases = {}
with open("glossary_aliases.txt") as f:
    for line in f:
        real, al = line.split("->")
        for name in shlex.split(al):
            aliases[name.strip()] = real.strip()


def missing_reference(app, env, node, contnode):
    target = node['reftarget']
    typ = node['reftype']
    fromdocname = node["refdoc"]
    if 'refdomain' in node and node['refdomain']:
        try:
            domain = env.domains[node['refdomain']]
        except KeyError:
            pass
    if node["reftarget"] in aliases and domain:
        node['reftarget'] = aliases[target]
        return domain.resolve_xref(env, fromdocname, app.builder,
                                   typ, aliases[target], node, contnode)
    if node["reftarget"].startswith("chapter") or node["reftarget"].startswith("appendix"):
        chap, appe = re.search("chapter (\d+)|appendix (\w+)", node["reftarget"]).groups()
        if chap:
            chap_lookup = dict(enumerate(env.toctree_includes["index"]))
            file = chap_lookup[int(chap)]
        elif appe:
            app_lookup = {chr(i + ord("a")): j for i, j in enumerate(env.config["latex_appendices"])}
            file = app_lookup[appe]
        else:
            RuntimeError("Panic, regex failed!")
        subref = "".join((x if x.isalpha() else "-") for x in file.split("/")[-1].lower()).rstrip("-")
        ref = file + ":" + subref
        node['reftarget'] = subref
        node['refexplicit'] = True
        #print(subref, domain, fromdocname, typ)
        #print(domain.data['anonlabels'])
        return sphinxnodes.make_refnode(app.builder, fromdocname, file, subref, contnode)


def setup(app):
    app.add_config_value('inline_highlight_literals', True, 'env')
    app.add_config_value('inline_highlight_respect_highlight', True, 'env')
    app.connect("missing-reference", missing_reference)
    sphinx.writers.latex.LaTeXTranslator = ISLLaTeXTranslator
