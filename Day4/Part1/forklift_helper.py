
filename = "Day4/Part1/input.txt"

def check_position_for_surroundings(board, pox_x, pox_y):
    # Check if the position is empty
    if(board[pox_y][pox_x] == "."):
        return False, 0
    
    # Check surroundings
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),           (1, 0),
                  (-1, 1), (0, 1),   (1, 1)]
    
    surrounding_rolls = 0

    for direction in directions:
        dx, dy = direction
        x, y = pox_x + dx, pox_y + dy

        # Check boundaries
        if 0 <= x < len(board[0]) and 0 <= y < len(board):
            if board[y][x] == "@":
                surrounding_rolls += 1
    
    return True, surrounding_rolls
     

with open(filename) as f:
    board = f.read().splitlines()

count = 0

for x, y in [(x, y) for y in range(len(board)) for x in range(len(board[0]))]:
    is_occupied, surrounding_rolls = check_position_for_surroundings(board, x, y)
  
    if is_occupied and surrounding_rolls < 4:
        count += 1

print("Count of positions with less than 4 surrounding rolls:", count)