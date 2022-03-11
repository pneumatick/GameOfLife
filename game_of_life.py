import random
import time
import os

# Create a dead board
def dead_state(width, height):
    board = []
    
    for i in range(width):
        board.append([])
        for j in range(height):
            board[i].append(0)

    return board

# Create a randomly generated board
def random_state(width, height):
    board = dead_state(width, height)

    for i in range(width):
        for j in range(height):
            # Generate a number from [0.0, 1.0)
            state = random.random()

            if state < 0.5:
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board

# Convert the board into a string that can be printed to a console
def render(raw_board):
    rendered_board = ""

    for i in range(len(raw_board)):
        for j in range(len(raw_board[i])):
            if raw_board[i][j] == 0:
                rendered_board += " "
            else:
                rendered_board += "#"
        rendered_board += '\n'

    print(rendered_board)

def next_board_state(pre_board):
    new_board = dead_state(len(pre_board), len(pre_board[0]))

    # Iterate over the board
    for i in range(len(pre_board)):
        for j in range(len(pre_board[i])):
            lower_x = i - 1
            upper_x = i + 2
            lower_y = j - 1
            upper_y = j + 2
            
            # Adjust the upper and/or lower bounds of the search if the cell
            # is on an edge
            if 0 < i < len(pre_board) - 1 and 0 < j < len(pre_board[i]) - 1:
                pass                
            else:
                if i == 0:
                    lower_x = i
                if i == len(pre_board) - 1:
                    upper_x = i + 1
                if j == 0:
                    lower_y = j
                if j == len(pre_board[i]) - 1:
                    upper_y = j + 1                

            live_cells = 0

            # Check for live cells around the current cell
            for u in range(lower_x, upper_x):
                for w in range(lower_y, upper_y):
                    # Count the live cells (skip self)
                    if u == i and w == j:
                        pass
                    elif pre_board[u][w] == 1:
                        live_cells += 1

            # Determine the cell's next state
            if pre_board[i][j] == 1:
                if 1 < live_cells < 4:
                    new_board[i][j] = 1
            else:
                if live_cells == 3:
                    new_board[i][j] = 1
            
    return new_board

s = random_state(40, 100) 
while True:
    time.sleep(1)
    os.system("CLS")
    render(s)
    s = next_board_state(s)
