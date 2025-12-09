import numpy as np

filename = "Day4/Part1/input.txt"

def check_position_for_surroundings(board, pos_x, pos_y):
    # Check if the position is empty
    if board[pos_x][pos_y] == ".":
        return False, 0
    
    if board[pos_x][pos_y] == "x":
        return False, 0
    
    # Check surroundings
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),           (1, 0),
                  (-1, 1), (0, 1),   (1, 1)]
    
    surrounding_rolls = 0

    for direction in directions:
        dx, dy = direction
        x, y = pos_x + dx, pos_y + dy

        # Check boundaries
        if 0 <= x < len(board[0]) and 0 <= y < len(board):
            if board[x][y] == "@":
                surrounding_rolls += 1
    
    return True, surrounding_rolls


def mark_position_for_removal(board, pos_x, pos_y):
    board[pos_x][pos_y] = "x"


def mark_positions_as_free(board, pos_x, pos_y):
    if board[pos_x][pos_y] == "x":
        board[pos_x][pos_y] = "."
        return True
    
    return False


def print_board(board):
    print("Current board: \n")
    for line in board:
        for pos in line:
            print("{}".format(pos).rjust(3), end="")
        print(end="\n")
    
    print("\n")


with open(filename) as f:
    board = [list(line) for line in f.read().splitlines()]

removed_rolls_count = 0
removals_possible = True

while removals_possible:
    removals_done_this_round = 0
    print_board(board)

    for x, y in [(x, y) for y in range(len(board)) for x in range(len(board[0]))]:
        result = mark_positions_as_free(board, x, y)

        if result:
            continue

        is_occupied, surrounding_rolls = check_position_for_surroundings(board, x, y)
    
        if is_occupied and surrounding_rolls < 4:
            removed_rolls_count += 1
            removals_done_this_round += 1
            mark_position_for_removal(board, x, y)

    if removals_done_this_round == 0:
        removals_possible = False

print("Count of positions with less than 4 surrounding rolls:", removed_rolls_count)