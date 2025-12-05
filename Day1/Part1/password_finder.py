import re

from Dial import Dial

filename = "Day1/Part1/input.txt"
startNumber = 50

dial = Dial(startNumber)

with open(filename) as file:
    for line in file:
        match = re.match(r"([a-z]+)([0-9]+)", line.strip(), re.I)
        if match:
            direction = match.group(1)
            distance = int(match.group(2))

            if direction == "R":
                dial.turn_right(distance)
            elif direction == "L":
                dial.turn_left(distance)

print("The dial had the position 0 a total of {} times.".format(dial.get_zero_count()))