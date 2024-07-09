import ply.lex as lex

# Liste des tokens
tokens = (
    'NUMBER', 'IDENTIFIER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQ', 'LT', 'GT', 'LE', 'GE', 'EQEQ', 'NE', 'SEMI',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'QUOTE', 'LET', 'IF', 'ELSE', 'PRINT'
)

# Règles simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQEQ = r'=='
t_NE = r'!='
t_SEMI = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_QUOTE = r'"'

# Règles pour les mots-clés
def t_LET(t):
    r'let'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

# Règle pour les identifiants (noms de variables)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Règle pour les nombres
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Règle pour ignorer les espaces et les tabulations
t_ignore = ' \t'

# Règle pour gérer les nouvelles lignes
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Règle pour gérer les erreurs
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construction de l'analyseur lexical
lexer = lex.lex()
