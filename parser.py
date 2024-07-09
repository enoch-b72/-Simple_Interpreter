import ply.yacc as yacc
from lexer import tokens

# Définitions des règles de la grammaire
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : let_statement
                 | print_statement
                 | if_statement'''
    p[0] = p[1]

def p_let_statement(p):
    '''let_statement : LET IDENTIFIER EQ expression SEMI'''
    p[0] = ('let', p[2], p[4])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN SEMI
                       | PRINT LPAREN QUOTE string QUOTE RPAREN SEMI'''
    if len(p) == 7:
        p[0] = ('print', p[3])
    else:
        p[0] = ('print', p[4])

def p_if_statement(p):
    '''if_statement : IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                    | IF expression LBRACE statement_list RBRACE'''
    if len(p) == 10:
        p[0] = ('if_else', p[2], p[4], p[8])
    else:
        p[0] = ('if', p[2], p[4])

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression LT term
                  | expression GT term
                  | expression LE term
                  | expression GE term
                  | expression EQEQ term
                  | expression NE term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_factor(p):
    '''factor : NUMBER
              | IDENTIFIER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_string(p):
    '''string : IDENTIFIER
              | string IDENTIFIER'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ' ' + p[2]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()
