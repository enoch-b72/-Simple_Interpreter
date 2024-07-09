# interpreter.py

def execute_program(program):
    env = {}
    for statement in program[1]:
        execute_statement(statement, env)

def execute_statement(statement, env):
    if statement[0] == 'let':
        env[statement[1]] = execute_expression(statement[2], env)
    elif statement[0] == 'print':
        print(statement[1])
    elif statement[0] == 'if_else':
        condition = execute_expression(statement[1], env)
        if condition:
            for stmt in statement[2]:
                execute_statement(stmt, env)
        else:
            for stmt in statement[3]:
                execute_statement(stmt, env)

def execute_expression(expr, env):
    if isinstance(expr, int):
        return expr
    elif isinstance(expr, str):
        return env[expr]
    elif isinstance(expr, tuple):
        if expr[0] == '+':
            return execute_expression(expr[1], env) + execute_expression(expr[2], env)
        elif expr[0] == '-':
            return execute_expression(expr[1], env) - execute_expression(expr[2], env)
        elif expr[0] == '<':
            return execute_expression(expr[1], env) < execute_expression(expr[2], env)
        elif expr[0] == '>':
            return execute_expression(expr[1], env) > execute_expression(expr[2], env)
        elif expr[0] == '<=':
            return execute_expression(expr[1], env) <= execute_expression(expr[2], env)
        elif expr[0] == '>=':
            return execute_expression(expr[1], env) >= execute_expression(expr[2], env)
        elif expr[0] == '==':
            return execute_expression(expr[1], env) == execute_expression(expr[2], env)
        elif expr[0] == '!=':
            return execute_expression(expr[1], env) != execute_expression(expr[2], env)

# Vous pourriez ajouter d'autres fonctions auxiliaires selon les besoins
