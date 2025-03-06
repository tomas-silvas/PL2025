import ply.lex as lex


# List of token names. This is always required
tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'VAR',
    'PREFIXED_NAME',
    'LITERAL',
    'DOT',
    'LBRACE',
    'RBRACE',
    'A',
    'NUMBER'
)

# Regular expression rules for simple tokens
t_SELECT = r'select'
t_WHERE = r'where'
t_LIMIT = r'LIMIT'
t_DOT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_A = r'a'

# A regular expression rule with some action code
def t_VAR(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_LITERAL(t):
    r'\"([^\\\"]|\\.)*\"(@[a-zA-Z]+)?'
    return t

def t_PREFIXED_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
    
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

data = '''
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
'''

def main():
    lexer.input(data)
    for tok in lexer:
        print(tok)

if __name__ == '__main__':
    main()