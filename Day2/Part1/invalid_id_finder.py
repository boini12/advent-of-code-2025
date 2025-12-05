import re

filename = "Day2/Part1/input.txt"

id_ranges = []
id_range_min : int
id_range_max : int

result = 0

re_pattern = r"(\d+)\1"

with open(filename,"r") as f:
    text = f.read()
    id_ranges = text.split(",")

    for id_range in id_ranges:
        id_range_split = id_range.split("-")
        id_range_min = int(id_range_split[0])
        id_range_max = int(id_range_split[1])

        for id in range(id_range_min, id_range_max + 1):
            id_to_check = str(id)
            # Skip odd length IDs - they cannot have an invalid id
            if(len(id_to_check) % 2 != 0):
                continue
            match = re.fullmatch(re_pattern, id_to_check)
            if(match is not None):
                result += id

print("The sum of all invalid IDs is: {}".format(result))

