import time
from random import randrange


class Game:
    BOARDSIZE = 0

    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        letterAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        # Generating board size
        while True:
            try:
                self.boardsize = int(input('enter size of the board: '))
            except ValueError:
                print("Invalid Input.")
                continue
            else:
                if 3 <= self.boardsize <= 10:
                    break
                else:
                    print("Invalid Input")
                    continue

        # Generating number of blocs
        while True:
            try:
                self.nbrOfBlocs = int(input('enter number of blocs: '))
            except ValueError:
                print("Invalid Input.")
                continue
            else:
                if 0 <= self.nbrOfBlocs <= 2 * self.boardsize:
                    break
                else:
                    print("Invalid Input.")
                    continue

        # Generating win condition
        while True:
            try:
                self.win_condition = int(input('enter win condition: '))
            except ValueError:
                print("Invalid Input.")
                continue
            else:
                if 3 <= self.win_condition <= self.boardsize:
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
        for i in range(self.nbrOfBlocs):
            bloc_coordinate_x = randrange(self.boardsize)
            bloc_coordinate_y = randrange(self.boardsize)
            blocXIndex.append(bloc_coordinate_x)
            blocYIndex.append(bloc_coordinate_y)

        # Generating board axis
        self.current_state = []
        letter_separator = ['  ']
        separator = [' +']
        for i in range(self.boardsize):
            letter_separator.append(letterAxis[i])
            separator.append('-')

        self.current_state.append(letter_separator)
        self.current_state.append(separator)

        # Populating board array
        bloc_placed = False
        for y in range(self.boardsize):
            row = [str(y) + '|']
            for x in range(self.boardsize):
                for i in range(self.nbrOfBlocs):
                    if blocXIndex[i] == x and blocYIndex[i] == y:
                        row.append('*')
                        bloc_placed = True
                        break

                if bloc_placed:
                    bloc_placed = False
                else:
                    row.append('.')
            self.current_state.append(row)

    def player_input(self):
        # hard coded - change
        self.current_state[3][1] = 'X'
        self.current_state[3][2] = 'X'
        self.current_state[3][3] = 'X'
        self.current_state[3][4] = 'X'

    def draw_board(self):
        print()
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                print(F'{self.current_state[y][x]}', end="")
            print()
        print()

    def is_end(self):
        # Horizontal check
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if self.current_state[y][x] != '-' and self.current_state[y][x] != '.' and x + 1 <= self.boardsize and \
                        self.current_state[y][x] == \
                        self.current_state[y][x + 1]:
                    horizontalWinCount += 1
                    if horizontalWinCount + 1 == self.win_condition:
                        return self.current_state[y][x]
            horizontalWinCount = 0

        # Vertical check
        for x in range(self.boardsize + 1):
            for y in range(self.boardsize + 2):
                if self.current_state[y][x] != '.' and y + 1 <= self.boardsize + 1 and self.current_state[y][x] == \
                        self.current_state[y + 1][x]:
                    verticalWinCount += 1
                    if verticalWinCount + 1 == self.win_condition:
                        return self.current_state[y][x]
            verticalWinCount = 0

        # Main diagonal check
        checkX = 1
        checkY = 2
        mainDiagonalWinCount = 0
        for i in range(self.boardsize):
            if self.current_state[checkY][
                checkX] != '.' and checkX + 1 <= self.boardsize and checkY + 1 <= self.boardsize + 1 and \
                    self.current_state[checkY][checkX] == self.current_state[checkY + 1][checkX + 1]:
                mainDiagonalWinCount += 1
                if mainDiagonalWinCount + 1 == self.win_condition:
                    return self.current_state[checkY][checkX]
                checkX += i
                checkY += i

        # Secondary diagonal check
        checkX = 1
        checkY = self.boardsize + 1
        secondaryDiagonalWinCount = 0
        for i in range(self.boardsize):
            if self.current_state[checkY][checkX] != '.' and checkX + 1 <= self.boardsize and checkY - 1 >= 0 and \
                    self.current_state[checkY][checkX] == self.current_state[checkY - 1][checkX + 1]:
                secondaryDiagonalWinCount += 1
                if secondaryDiagonalWinCount + 1 == self.win_condition:
                    return self.current_state[checkY][checkX]
                checkX += i
                checkY -= i

        # diagonal check
        diagonalCheck = 0
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if self.current_state[y][x] == 'X' or self.current_state[y][x] == 'O':
                    for i in range(self.win_condition):
                        if x + i <= self.boardsize and y + i <= self.boardsize + 1 and (
                                self.current_state[y][x] == self.current_state[y + i][x + i] or self.current_state[y][
                            x] ==
                                self.current_state[y - i][x - i]):
                            diagonalCheck += 1
                            if diagonalCheck == self.win_condition:
                                return self.current_state[y][x]

        # Check if empty
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if (self.current_state[y][x] == '.'):
                    return None
        # it's a tie
        return '.'

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

    def play(self):
        while True:
            self.draw_board()
            if self.is_end():
                print("Winner is found")
                return
            self.player_input()


def main():
    g = Game()
    g.play()


if __name__ == "__main__":
    main()
