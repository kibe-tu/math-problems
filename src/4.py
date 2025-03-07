import random

def solve_math_problem(n):
    problem = "What is the sum of " + str(random.randint(1, n)) + " and " + str(random.randint(1, n)) + "?"
    return problem

# Example usage:

solve_math_problem(5)
