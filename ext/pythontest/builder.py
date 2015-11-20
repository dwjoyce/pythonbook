from docutils import nodes
from docutils.io import FileOutput
from docutils.utils import new_document
from docutils.frontend import OptionParser

from sphinx import package_dir, addnodes
from sphinx.util import texescape
from sphinx.locale import _
import sphinx.builders
from sphinx.environment import NoUri
from sphinx.util.nodes import inline_all_toctrees
from sphinx.util.osutil import SEP, copyfile
from sphinx.util.console import bold, darkgreen
from sphinx.writers.latex import LaTeXWriter
from os import path
from . import writer

app = None


class Builder(sphinx.builders.Builder):
    """
    Builds LaTeX output to create PDF.
    """
    name = 'pythontest'
    format = 'pythontest'
    supported_image_types = ['application/pdf', 'image/png',
                             'image/gif', 'image/jpeg']

    def init(self):
        self.docnames = []
        self.document_data = []

    def get_outdated_docs(self):
        return 'all documents' # for now

    def get_target_uri(self, docname, typ=None):
        if docname not in self.docnames:
            raise NoUri
        else:
            return '%' + docname

    def get_relative_uri(self, from_, to, typ=None):
        # ignore source path
        return self.get_target_uri(to, typ)

    def init_document_data(self):
        preliminary_document_data = list(map(list, self.config.latex_documents))
        if not preliminary_document_data:
            self.warn('no "latex_documents" config value found; no documents '
                      'will be written')
            return
        # assign subdirs to titles
        self.titles = []
        for entry in preliminary_document_data:
            docname = entry[0]
            if docname not in self.env.all_docs:
                self.warn('"latex_documents" config value references unknown '
                          'document %s' % docname)
                continue
            self.document_data.append(entry)
            self.titles.append((docname, entry[2]))

    def write(self, *ignored):
        docwriter = writer.Writer(self)
        docsettings = OptionParser(
            defaults=self.env.settings,
            components=(docwriter,),
            read_config_files=True).get_default_values()

        self.init_document_data()

        for entry in self.document_data:
            docname, targetname, title, author, docclass = entry[:5]
            targetname = targetname.replace(".tex", ".pyt")
            toctree_only = False
            if len(entry) > 5:
                toctree_only = entry[5]
            destination = FileOutput(
                destination_path=path.join(self.outdir, targetname),
                encoding='utf-8')
            self.info("processing " + targetname + "... ", nonl=1)
            doctree = self.assemble_doctree(docname, toctree_only,
                appendices=((docclass != 'howto') and
                            self.config.latex_appendices or []))
            #print(doctree)
            self.post_process_images(doctree)
            self.info("writing... ", nonl=1)
            doctree.settings = docsettings
            doctree.settings.author = author
            doctree.settings.title = title
            doctree.settings.docname = docname
            doctree.settings.docclass = docclass
            docwriter.write(doctree, destination)
            self.info("done")
        docwriter.set_returncode(app)

    def assemble_doctree(self, indexfile, toctree_only, appendices):
        self.docnames = set([indexfile] + appendices)
        self.info(darkgreen(indexfile) + " ", nonl=1)
        tree = self.env.get_doctree(indexfile)
        tree['docname'] = indexfile
        if toctree_only:
            # extract toctree nodes from the tree and put them in a
            # fresh document
            new_tree = new_document('<pythonbook output>')
            new_sect = nodes.section()
            new_sect += nodes.title('<Set title in conf.py>',
                                    '<Set title in conf.py>')
            new_tree += new_sect
            for node in tree.traverse(addnodes.toctree):
                new_sect += node
            tree = new_tree
        largetree = inline_all_toctrees(self, self.docnames, indexfile, tree,
                                        darkgreen)
        largetree['docname'] = indexfile
        for docname in appendices:
            appendix = self.env.get_doctree(docname)
            appendix['docname'] = docname
            largetree.append(appendix)
        self.info()
        self.info("resolving references...")
        self.env.resolve_references(largetree, indexfile, self)
        # resolve :ref:s to distant tex files -- we can't add a cross-reference,
        # but append the document name
        for pendingnode in largetree.traverse(addnodes.pending_xref):
            docname = pendingnode['refdocname']
            sectname = pendingnode['refsectname']
            newnodes = [nodes.emphasis(sectname, sectname)]
            for subdir, title in self.titles:
                if docname.startswith(subdir):
                    newnodes.append(nodes.Text(_(' (in '), _(' (in ')))
                    newnodes.append(nodes.emphasis(title, title))
                    newnodes.append(nodes.Text(')', ')'))
                    break
            else:
                pass
            pendingnode.replace_self(newnodes)
        return largetree

    def finish(self):
        self.info('done')
