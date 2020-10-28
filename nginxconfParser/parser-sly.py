from sly import Lexer,Parser

text = """
server {
    location / {
	# Проверка коменнтариев
        fastcgi_pass  localhost:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param QUERY_STRING    $query_string;
    }

    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
       """

class conf(Lexer):
    tokens = {BGN,END,NM,SEMIC}
    BGN = r'{'
    END = r'}'
    NM = r'[^\t\#{};]+'
    SEMIC = r';'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'
    ignore = r' \t'

class parse(Parser):
    tokens = conf.tokens

    # Декратор для описания правил
    @_('directive directives')
    def directives(self,p):
        pass

    @_('empty')
    def directives(self,p):
        pass
    
    @_('directive','block')
    def directives(self,p):
        pass

    @_('name names BGN directives END')
    def block(self,p):
        pass

    @_('NAME names')
    def names(self,p):
        pass

    @_('empty')
    def names(self,p):
        pass

    @_('')
    def empty(self,p):
        pass

"""
lexem = conf()
pasrer = parse()
print(pasrer.parse(lexem.tokinez(text)))
"""

lexer = conf()
for token in lexer.tokenize(text):
    print(token)
