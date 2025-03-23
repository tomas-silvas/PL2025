import ply.lex as lex


# List of token names. This is always required
tokens = (
    'NUM',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'LPAREN',
    'RPAREN'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A regular expression rule with some action code
def t_NUM(t):
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