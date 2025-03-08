import random

def get_random_math_problem():
    operands = [random.randint(1, 10), random.randint(1, 10)]
    operation = random.choice(['+', '-', '*', '/'])
    answer = operands[0] + operands[1]
    if operation == '+':
        return f'{operands[0]} + {operands[1]} = {answer}'
    elif operation == '-':
        return f'{operands[0]} - {operands[1]} = {answer}'
    elif operation == '*':
        return f'{operands[0]} * {operands[1]} = {answer}'
    else:
        return f'{operands[0]} / {operands[1]} = {answer}'
