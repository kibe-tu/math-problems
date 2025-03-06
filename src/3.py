def get_random_math_problem():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    if op == '+':
        return f'{num1} + {num2}'
    elif op == '-':
        return f'{num1} - {num2}'
    elif op == '*':
        return f'{num1} * {num2}'
    else:
        return f'{num1} / {num2}'
