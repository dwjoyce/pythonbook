import re

from pygments import lexers
from pygments.lexers import Python3Lexer

from pygments.lexer import Lexer, RegexLexer, ExtendedRegexLexer, \
     LexerContext, include, combined, do_insertions, bygroups, using
from pygments.token import Error, Text, Other, \
     Comment, Operator, Keyword, Name, String, Number, Generic, Punctuation
from pygments.util import get_bool_opt, get_list_opt, shebang_matches
from pygments import unistring as uni

__all__ = ["Python3ConsoleLexer"]

line_re  = re.compile('.*?\n')

class Python3TracebackLexer(RegexLexer):
    """
    For Python 3.0 tracebacks, with support for chained exceptions.

    *New in Pygments 1.0.*
    """

    name = 'Python 3.0 Traceback'
    aliases = ['py3tb']
    filenames = ['*.py3tb']
    mimetypes = ['text/x-python3-traceback']

    tokens = {
        'root': [
            (r'\n', Text),
            (r'^Traceback \(most recent call last\):\n', Generic.Traceback, 'intb'),
            (r'^During handling of the above exception, another '
             r'exception occurred:\n\n', Generic.Traceback),
            (r'^The above exception was the direct cause of the '
             r'following exception:\n\n', Generic.Traceback),
            (r'^(File )("[^"]+")(, line )(\d+)(\n)',
             bygroups(Text, Name.Builtin, Text, Number, Text), 'intb')
        ],
        'intb': [
            (r'^(  File )("[^"]+")(, line )(\d+)(, in )(.+)(\n)',
             bygroups(Text, Name.Builtin, Text, Number, Text, Name, Text)),
            (r'^(    )(.+)(\n)',
             bygroups(Text, using(Python3Lexer), Text)),
            (r'^([ \t]*)(\.\.\.)(\n)',
             bygroups(Text, Comment, Text)), # for doctests...
            (r'^([^:]+)(: )(.+)(\n)',
             bygroups(Generic.Error, Text, Name, Text), '#pop'),
            (r'^([a-zA-Z_][a-zA-Z0-9_]*)(:?\n)',
             bygroups(Generic.Error, Text), '#pop')
        ],
    }


class Python3ConsoleLexer(Lexer):
    """
    For Python console output or doctests, such as:

    .. sourcecode:: pycon

        >>> a = 'foo'
        >>> print a
        foo
        >>> 1 / 0
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        ZeroDivisionError: integer division or modulo by zero

    Additional options:

    `python3`
        Use Python 3 lexer for code.  Default is ``False``.
        *New in Pygments 1.0.*
    """
    name = 'Python 3 console session'
    aliases = ['pycon3']
    mimetypes = ['text/x-python-doctest']

    def get_tokens_unprocessed(self, text):
        if "if broken = True" not in text:
            dprint = lambda *a: None
        else:
            dprint = print
        pylexer = Python3Lexer(**self.options)
        tblexer = Python3TracebackLexer(**self.options)
        dprint(repr(text))
        if ">>>" not in text:
            if (text.startswith('Traceback (most recent call last):') or
                        re.match(r'^  File "[^"]+", line \d+\n$', text)):
                yield from tblexer.get_tokens_unprocessed(text)
            else:
                yield from pylexer.get_tokens_unprocessed(text)
            return

        curcode = ''
        insertions = []
        curtb = ''
        tbindex = 0
        tb = 0


        def do_current_code():
            nonlocal curcode
            nonlocal insertions
            if curcode:
                for item in do_insertions(insertions,
                                          pylexer.get_tokens_unprocessed(curcode)):
                    yield item
                curcode = ''
                insertions = []

        #lines = line_re.finditer(text)
        #for match in :
            #line = match.group()
            #if line.startswith('>>> ') or line.startswith('    ') and not tb:
                #tb = 0
                #insertions.append((len(curcode),
                                   #[(0, Generic.Prompt, line[:4])]))
                #curcode += line[4:]
            #elif line.rstrip() == '...' and not tb:
                ## only a new >>> prompt can end an exception block
                ## otherwise an ellipsis in place of the traceback frames
                ## will be mishandled
                #insertions.append((len(curcode),
                                   #[(0, Generic.Prompt, '...')]))
                #curcode += line[3:]
            #else:
                #do_current_code()
                #if (line.startswith('Traceback (most recent call last):') or
                    #re.match(r'  File "[^"]+", line \d+\n$', line)):
                    #tb = 1
                    #curtb = line
                    #tbindex = match.start()
                #elif line == 'KeyboardInterrupt\n':
                    #yield match.start(), Name.Class, line
                #elif tb:
                    #curtb += line
                    #if not (line.startswith(' ') or line.strip() == '...'):
                        #tb = 0
                        #for i, t, v in tblexer.get_tokens_unprocessed(curtb):
                            #yield tbindex+i, t, v
                #else:
                    #yield match.start(), Generic.Output, line
        #if curcode:
            #for item in do_insertions(insertions,
                                      #pylexer.get_tokens_unprocessed(curcode)):
                #yield item
        section = ""
        
        code = list(line_re.finditer(text))
        dprint(code)
        while code:
            match = code.pop(0)
            line = match.group()
            dprint(line)
            if line.startswith(">>>"):
                insertions = []
                insertions.append((0,
                                   [(0, Generic.Prompt, line[:4])]))
                section = line[4:]
                secindex = match.start()
                while code and code[0].group().startswith("   "):
                    line = code.pop(0).group()
                    if not line.strip():
                        break
                    insertions.append((len(section),
                                        [(0, Generic.Prompt, line[:4])]))
                    section += line[4:]
                dprint("SECTION", repr(section))
                for i, t, v in do_insertions(insertions,
                                            pylexer.get_tokens_unprocessed(section)):
                    #if t == Error:
                    dprint(i, t, v)
                    yield secindex+i, t, v
            elif line.startswith('Traceback (most recent call last):') or re.match(r' *File "[^"]+", line \d+\n$', line):
                tb = line
                tbindex = match.start()
                while code and not code[0].group().startswith(">>>"):
                    tb += code.pop(0).group()
                dprint("TB", repr(tb))
                for i, t, v in tblexer.get_tokens_unprocessed(tb):
                    dprint(i, t, v)
                    yield tbindex+i, t, v
            else:
                yield match.start(), Generic.Output, line


lexers._mapping.LEXERS["Python3ConsoleLexer"] = ('lexer', 'Python3ConsoleLexer', ('py3con'), (), ('text/x-python3', 'application/x-python3'))
lexers._lexer_cache["Python3ConsoleLexer"] = Python3ConsoleLexer
#lexers.Python3ConsoleLexer = Python3ConsoleLexer

print(lexers.get_lexer_by_name("py3con"))

def setup(app):
    pass
