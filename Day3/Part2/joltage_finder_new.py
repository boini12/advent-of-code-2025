
filename = "Day3/Part1/input.txt"

max_number_of_batteries = 12
sum_of_max_joltage = 0

with open(filename) as file:
    for line in file:
        len_of_line = len(line.strip())

        dict_of_batteries = {index: int(value) for index, value in enumerate(line.strip())}
        sorted_dict_of_batteries_by_value = dict(sorted(dict_of_batteries.items(), key=lambda item: item[1], reverse=True))

        valid_keys = [key for key, _ in sorted_dict_of_batteries_by_value.items() if key <= len_of_line - max_number_of_batteries]
        
        highest_joltage_battery_key = valid_keys[0]

        # Select the first highest battery that still allows enough space for the remaining batteries
        first_battery_joltage = dict_of_batteries[highest_joltage_battery_key]

        del dict_of_batteries[highest_joltage_battery_key]

        remaining_line = line.strip()[highest_joltage_battery_key + 1:]
        
        selected_digits = []
        current_pos = 0
        
        # First battery is already selected
        digits_needed = max_number_of_batteries - 1
        
        while digits_needed > 0 and current_pos < len(remaining_line):
            positions_available = len(remaining_line) - current_pos
            # Calculate the maximum number of positions we can skip to still fit the remaining digits
            max_skip = positions_available - digits_needed
            
            largest_digit = 0
            largest_pos = current_pos
            
            for pos in range(current_pos, current_pos + max_skip + 1):
                if int(remaining_line[pos]) > largest_digit:
                    largest_digit = int(remaining_line[pos])
                    largest_pos = pos
            
            selected_digits.append(largest_digit)
            current_pos = largest_pos + 1
            digits_needed -= 1
        
        max_joltage_for_line = str(first_battery_joltage) + ''.join(map(str, selected_digits))
        sum_of_max_joltage += int(max_joltage_for_line)

print(sum_of_max_joltage)