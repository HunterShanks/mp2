import time
from random import randrange


class Game:
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
        # ---------------------------------------------------------
        blocXIndex = []
        blocYIndex = []
        for i in range(self.nbrOfBlocs):
            bloc_coordinate_x = randrange(self.boardsize)
            bloc_coordinate_y = randrange(self.boardsize)
            blocXIndex.append(bloc_coordinate_x)
            blocYIndex.append(bloc_coordinate_y)
        # ---------------------------------------------------------

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

    def player_input1(self):
        self.current_state[2][1] = '*'
        self.current_state[5][2] = 'O'
        self.current_state[4][3] = 'O'
        self.current_state[3][4] = 'O'

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
                        self.current_state[y][x] == self.current_state[y][x + 1]:
                    horizontalWinCount += 1
                    if horizontalWinCount + 1 == self.win_condition:
                        print(self.current_state[y][x], "Horizontal win")
                        return self.current_state[y][x]
            horizontalWinCount = 0

        # Vertical check
        for x in range(self.boardsize + 1):
            for y in range(self.boardsize + 2):
                if self.current_state[y][x] != '.' and y + 1 <= self.boardsize + 1 and self.current_state[y][x] == \
                        self.current_state[y + 1][x]:
                    verticalWinCount += 1
                    if verticalWinCount + 1 == self.win_condition:
                        print(self.current_state[y][x], "Vertical win")
                        return self.current_state[y][x]
            verticalWinCount = 0

        # Diagonal check
        mainDiagonalWinCheck = 0
        secondaryDiagonalWinCheck = 0
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if y == self.boardsize+1:
                    return None
                if self.current_state[y][x] == 'X' or self.current_state[y][x] == 'O':
                    for i in range(self.win_condition):
                        if x+i <= self.boardsize and y + i <= self.boardsize+1 and self.current_state[y][x] == self.current_state[y+i][x+i]:
                            mainDiagonalWinCheck += 1
                            if mainDiagonalWinCheck == self.win_condition:
                                print(self.current_state[y][x], "main diagonal win")
                                return self.current_state[y][x]
                        elif x == 1:
                            secondaryDiagonalWinCheck = 0
                            break
                        elif x - i >= 1 and y + i <= self.boardsize+1 and self.current_state[y][x] == self.current_state[y+i][x-i]:
                            secondaryDiagonalWinCheck += 1
                            if secondaryDiagonalWinCheck == self.win_condition:
                                print(self.current_state[y][x], "secondary diagonal win")
                                return self.current_state[y][x]
                        else:
                            mainDiagonalWinCheck = 0
                            secondaryDiagonalWinCheck = 0
                            break

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
        player_turn = 'X'
        while True:
            self.draw_board()
            if self.check_end():
                return
            else:
                if player_turn == 'X':
                    print("Player X plays")
                    self.player_input1()
                #    player_turn = 'O'
                # elif player_turn == 'O':
                #     print("Player O plays")
                #     self.player_input2()
                #     player_turn = 'X'



def main():
    g = Game()
    g.play()
    


if __name__ == "__main__":
    main()
