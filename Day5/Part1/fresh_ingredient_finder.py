from FreshId import FreshId

filename = "Day5/Part1/input.txt"

ingredient_ids = []
reading_ids = False
freshIds = []
fresh_ingredients_count = 0

def is_empty_line(line) -> bool:
    if line == "":
        return True
    
    return False


def extract_ingredient_ids(line):
    ingredient_ids.append(int(line))


def extract_ranges(line):
    ranges = line.split("-")
    freshIds.append(FreshId(int(ranges[0]), int(ranges[1])))


with open(filename) as f:
        database = f.read().splitlines()

        for line in database:
            if is_empty_line(line):
                reading_ids = True
                continue

            if reading_ids:
                extract_ingredient_ids(line)
            else:
                extract_ranges(line)

for id in ingredient_ids:
    for fresh_id in freshIds:
        result = fresh_id.check_Id_for_freshness(id)
        if result:
            fresh_ingredients_count += 1
            break

print(f"Fresh ingredients count: {fresh_ingredients_count}")



