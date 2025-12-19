
filename = "Day5/Part1/input.txt"

fresh_ids = []

def is_empty_line(line) -> bool:
    if line == "":
        return True
    
    return False


def extract_ranges(line):
    ranges = line.split("-")
    fresh_ids.append([int(ranges[0]), int(ranges[1])])


with open(filename) as f:
        database = f.read().splitlines()

        for line in database:
            if is_empty_line(line):
                break

            extract_ranges(line)

interval_ids = [(f[0], f[1]) for f in fresh_ids]

interval_ids.sort(key=lambda x: x[0])

merged_intervals = []
for start, end in interval_ids:
     if not merged_intervals:
          merged_intervals.append([start, end])
          continue
     last = merged_intervals[-1]
     if start <= last[1] + 1:
        last[1] = max(last[1], end)
     else:
        merged_intervals.append([start, end])

fresh_ingredients_count = sum(end - start + 1 for start, end in merged_intervals)
print(f"Fresh ingredients count: {fresh_ingredients_count}")
