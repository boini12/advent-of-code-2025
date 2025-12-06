
filename = "Day3/Part1/input_test.txt"

with open(filename) as file:
    for line in file:
        max_joltage = 0
        for index, digit in enumerate(line.strip()):
            for next_digit in line[index + 1:]:
                temp_joltage = digit + next_digit
                converted_temp_joltage = int(temp_joltage)
                if converted_temp_joltage > max_joltage:
                    max_joltage = converted_temp_joltage
            
        sum_of_max_joltage += max_joltage
        print(f"Max joltage for line: {max_joltage}")

print(f"Sum of max joltage values: {sum_of_max_joltage}")