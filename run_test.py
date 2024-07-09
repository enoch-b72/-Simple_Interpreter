from lexer import lexer
from parser import parser

with open('examples/example1.txt') as f:
    data = f.read()

lexer.input(data)
for tok in lexer:
    print(tok)

ast = parser.parse(data)
print(ast)
