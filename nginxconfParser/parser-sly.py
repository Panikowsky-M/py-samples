from pprint import pprint as prettify_out
from sly import Lexer,Parser


class conf(Lexer):
    tokens = {BEGIN,END,NAME,SEMICOLON}
    BEGIN = r'{'
    END = r'}'
    NAME = r'[^\t\#{};]+'
    SEMICOLON = r';'
    ignore = r' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

class confParse(Parser):
    tokens = conf.tokens

    # Декоратор для описания правил

    @_('directive directives')
    def directives(self,p):
        return [p.directive] + p.directives

    @_('empty')
    def directives(self,p):
        return []
    
    @_('simpledir','blockdir')
    def directive(self,p):
        return p[0]

    @_('NAME names SEMICOLON')
    def simpledir(self,p):
        return dict(type= "simple", val = [[p.NAME] + p.names], ctx=[])


    @_('NAME names BEGIN directives END')
    def blockdir(self,p):
        return dict(type = "block", val = [[p.NAME] + p.names], ctx=p.directives)

    @_('NAME names')
    def names(self,p):
        return [p.NAME] + p.names;

    @_('empty')
    def names(self,p):
        return []

    @_('')
    def empty(self,p):
        pass

text = """
user     www www;
worker_process 5; # Default
error_log logs/error.log;
pid       logs/nginx.pid;
worker_rlimit_nofile 8122;
"""

lexer = conf()
parser = confParse()
prettify_out(parser.parse(lexer.tokenize(text)))
