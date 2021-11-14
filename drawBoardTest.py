import random
from random import randrange

# def initialize_game(self): --------------------------------------------------------
letterAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Generating board size
while True:
    try:
        boardsize = int(input('enter size of the board: '))
    except ValueError:
        print("Invalid Input.")
        continue
    else:
        if 3 <= boardsize <= 10:
            break
        else:
            print("Invalid Input")
            continue

# Generating number of blocs
while True:
    try:
        nbrOfBlocs = int(input('enter number of blocs: '))
    except ValueError:
        print("Invalid Input.")
        continue
    else:
        if 0 <= nbrOfBlocs <= 2 * boardsize:
            break
        else:
            print("Invalid Input.")
            continue

# Generating win condition
while True:
    try:
        win_condition = int(input('enter win condition: '))
    except ValueError:
        print("Invalid Input.")
        continue
    else:
        if 3 <= win_condition <= boardsize:
            break
        else:
            print("Invalid Input.")
            continue

# Generating Blocs

    # FOR GAMETRACE 4435 AND 4431
    # blocXIndex = [0, 0, 4, 4]
    # blockYIndex = [0, 4, 0, 4]

blocXIndex = []
blocYIndex = []
for i in range(nbrOfBlocs):
    bloc_coordinate_x = randrange(boardsize)
    bloc_coordinate_y = randrange(boardsize)
    blocXIndex.append(bloc_coordinate_x)
    blocYIndex.append(bloc_coordinate_y)

# Generating board axis
current_state = []
letter_separator = ['  ']
separator = [' +']
for i in range(boardsize):
    letter_separator.append(letterAxis[i])
    separator.append('-')

current_state.append(letter_separator)
current_state.append(separator)

# Populating board array
bloc_placed = False
for y in range(boardsize):
    row = [str(y) + '|']
    for x in range(boardsize):
        for i in range(nbrOfBlocs):
            if blocXIndex[i] == x and blocYIndex[i] == y:
                row.append('*')
                bloc_placed = True
                break

        if bloc_placed:
            bloc_placed = False
        else:
            row.append('.')
    current_state.append(row)

# ---------------------------------------------------------------------------------------


# Testing purposes
# Checking horizontal win conditions 4x4
#current_state[3][1] = 'X'
#current_state[3][2] = 'X'
#current_state[3][3] = 'X'
#current_state[3][4] = 'X'

# Vertical win conditions 4x4
current_state[2][3] = 'O'
current_state[3][3] = 'O'
current_state[4][3] = 'O'
current_state[5][3] = 'O'

# Diagonal win conditions 4x4
#current_state[2][1] = 'X'
#current_state[3][2] = 'X'
#current_state[4][3] = 'X'
#current_state[5][4] = 'X'

# def is_end(self): ---------------------------------------------------------------------
# Horizontal check
for y in range(boardsize+2):
    for x in range(boardsize+1):
        if current_state[y][x] != '-' and current_state[y][x] != '.' and x+1 <= boardsize and current_state[y][x] == current_state[y][x+1]:
            horizontalWinCount += 1
            if horizontalWinCount+1 == win_condition:
                print(current_state[y][x], "horizontal win")  # change to return in skeleton
                break
    horizontalWinCount = 0

# Vertical check
for x in range(boardsize+1):
    for y in range(boardsize+2):
        if current_state[y][x] != '.' and y+1 <= boardsize+1 and current_state[y][x] == current_state[y+1][x]:
            verticalWinCount += 1
            if verticalWinCount+1 == win_condition:
                print(current_state[y][x], "vertical win")
                break
    verticalWinCount = 0

# Diagonal check

#  ---------------------------------------------------------------------------------------------------------

# [y] WILL ALWAYS HAVE +2 [x] WILL ALWAYS HAVE +1
#print(current_state)

# def draw_board(self): -------------------------------------------------------------------
print("Board Game")
print()
for y in range(boardsize+2):
    for x in range(boardsize+1):
        print(F'{current_state[y][x]}', end="")
    print()
print()

# ----------------------------------------------------------------------------------------