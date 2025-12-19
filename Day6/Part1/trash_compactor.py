import math

filename = "Day6/input.txt"
input_data = []
sum_of_all_problems = 0

def execute_operation(operation_char, items):
    if operation_char == '+':
        return sum(items)
    elif operation_char == '*':
        return math.prod(items)

with open(filename) as f:
    rows = [line.split() for line in f]

columns = zip(*rows)

for col in columns:
    input_data.append(col)

for problem in input_data:
    last = problem[-1]
    numbers = [int(x) for x in problem[:-1]]
    result = execute_operation(last, numbers)
    sum_of_all_problems += result

print(f"Sum of all problems: {sum_of_all_problems}")