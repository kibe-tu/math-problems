import random

def get_random_code():
    operators = ["+", "-", "*", "/"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_operators = random.randint(2, 3)
    code = ""
    for i in range(num_operators):
        op = operators[random.randint(0, len(operators) - 1)]
        num1 = numbers[random.randint(0, len(numbers) - 1)]
        num2 = numbers[random.randint(0, len(numbers) - 1)]
        code += str(num1) + " " + op + " " + str(num2) + "\n"
    return code