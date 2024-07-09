# main.py

from interpreter import execute_program

# Exemple d'exécution
program = ('program', [
    ('let', 'x', 10),
    ('let', 'y', 20),
    ('if_else', ('<', 'x', 'y'), [('print', 'x is less than y')], [('print', 'x is not less than y')])
])

execute_program(program)
