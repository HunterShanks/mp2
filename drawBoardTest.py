import random
from random import randrange

letterAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Generating board size
while True:
    try:
        boardsize = int(input('Enter size of the board: '))
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
        nbrOfBlocs = int(input('Enter number of blocs: '))
    except ValueError:
        print("Invalid Input.")
        continue
    else:
        if 0 <= nbrOfBlocs <= 2 * boardsize:
            break
        else:
            print("Invalid Input. Too many blocs")
            continue

# Generating goal state
while True:
    try:
        goalState = int(input('Enter win condition: '))
    except ValueError:
        print("Invalid Input.")
        continue
    else:
        if 3 <= goalState <= boardsize:
            break
        else:
            print("Invalid Input")
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

# Checking the goal state
def is_end(self):
    horizontalX = []
    horizontalO = []

    for i in range(goalState):
        horizontalX.append('X')
        horizontalO.append('O')

    # Vertical win
    winCount = 0
    for x in range(boardsize):
        for y in range(boardsize):
            if self.current_state[x][y] != "." and self.current_state[x][y] == self.current_state[x][y + 1] and (y + 1) <= boardsize:
                if winCount == goalState:
                    return self.current_state[x][y]
                else:
                    winCount += 1
        winCount = 0
    # Horizontal win
    for i in range(boardsize):
        if (self.current_state[i] == horizontalX):
            return 'X'
        elif (self.current_state[i] == horizontalO):
            return 'O'
    # # Main diagonal win
    # if (self.current_state[0][0] != '.' and
    #         self.current_state[0][0] == self.current_state[1][1] and
    #         self.current_state[0][0] == self.current_state[2][2]):
    #     return self.current_state[0][0]
    # # Second diagonal win
    # if (self.current_state[0][2] != '.' and
    #         self.current_state[0][2] == self.current_state[1][1] and
    #         self.current_state[0][2] == self.current_state[2][0]):
    #     return self.current_state[0][2]
    # # Is whole board full?
    # for i in range(0, 3):
    #     for j in range(0, 3):
    #         # There's an empty field, we continue the game
    #         if (self.current_state[i][j] == '.'):
    #             return None
    # # It's a tie!
    # return '.'


def input_move(self):
    while True:
        print(F'Player {self.player_turn}, enter your move:')
        px = int(input('enter the x coordinate: '))
        py = int(input('enter the y coordinate: '))
        if self.is_valid(px, py):
            return (px, py)
        else:
            print('The move is not valid! Try again.')


def is_valid(self, px, py):
    if px < 0 or px > boardsize or py < 0 or py > boardsize:
        return False
    elif self.current_state[px][py] != '.':
        return False
    else:
        return True


def check_end(self):
    self.result = self.is_end()
    # Printing the appropriate message if the game has ended
    if self.result != None:
        if self.result == 'X':
            print('The winner is X!')
        elif self.result == 'O':
            print('The winner is O!')
        elif self.result == '.':
            print("It's a tie!")
        self.initialize_game()
    return self.result

# # Horizontal check
# current_state[0][0] = 'X'
# current_state[1][0] = 'X'
# current_state[2][0] = 'X'
# current_state[3][0] = 'X'



# Drawing board
print("Board Game")
print()
for x in range(boardsize+2):
    for y in range(boardsize+1):
        print(F'{current_state[x][y]}', end="")
    print()
print()
check_end()
