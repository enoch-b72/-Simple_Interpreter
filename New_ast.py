class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

class LetStatement(Node):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

class PrintStatement(Node):
    def __init__(self, expression):
        self.expression = expression

class IfStatement(Node):
    def __init__(self, condition, true_branch, false_branch):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

class Expression(Node):
    pass

class BinaryOperation(Expression):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class Number(Expression):
    def __init__(self, value):
        self.value = value

class Identifier(Expression):
    def __init__(self, name):
        self.name = name
