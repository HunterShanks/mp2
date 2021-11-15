import time
import os
from random import randrange

class Game:
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
        # Player X always plays first
        self.player_turn = 'X'

    def is_valid(self, px, py):
        if px < 0 or px > self.boardsize or py < 0 or py > self.boardsize:
            return False
        elif self.current_state[px][py] != '.' and self.current_state[px][py] != '*':
            return False
        else:
            return True

    def player_input(self):
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = int(input('Enter the x coordinate (0 - '+ str(self.boardsize-1) + '): '))
            strY = str(input('Enter the y-letter coordinate: '))
            py = self.LETTERS.index(strY.upper())
            if self.is_valid(px+2 , py+1):
                return (px+2, py+1)
            else:
                print('The move is not valid! Try again.')

    # def player_input(self):
        # hard coded - change
        # self.current_state[3][1] = 'X'
        # self.current_state[3][2] = 'X'
        # self.current_state[3][3] = 'X'
        # self.current_state[3][4] = 'X'

        # # HARD CODED TIE 3x3
        # self.current_state[2][1] = 'O'
        # self.current_state[2][2] = 'X'
        # self.current_state[2][3] = 'O'
        # self.current_state[3][1] = 'O'
        # self.current_state[3][2] = 'X'
        # self.current_state[3][3] = 'O'
        # self.current_state[4][1] = 'X'
        # self.current_state[4][2] = 'O'
        # self.current_state[4][3] = 'X'



    def draw_board(self):
        print()
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                print(F'{self.current_state[y][x]}', end="")
            print()
        print()

    # def horizontalCheck(self):
    #     # Horizontal check
    #     for y in range(self.boardsize + 2):
    #         for x in range(self.boardsize + 1):
    #             if self.current_state[y][x] != '-' and self.current_state[y][x] != '.' and x + 1 <= self.boardsize and self.current_state[y][x] == self.current_state[y][x + 1]:
    #                 horizontalWinCount += 1
    #                 print("horizontal match found")
    #                 if horizontalWinCount + 1 == self.win_condition:
    #                     print(self.current_state[y][x], "Horizontal win")
    #                     return True
    #                     # return self.current_state[y][x]
    #         horizontalWinCount = 0
    #     return False
    #
    # def verticalCheck(self):
    #     # Vertical check
    #     for x in range(self.boardsize + 1):
    #         for y in range(self.boardsize + 2):
    #             if self.current_state[y][x] != '.' and y + 1 <= self.boardsize + 1 and self.current_state[y][x] == self.current_state[y + 1][x]:
    #                 verticalWinCount += 1
    #                 print("vertical match found")
    #                 if verticalWinCount + 1 == self.win_condition:
    #                     print(self.current_state[y][x], "Vertical win")
    #                     return True
    #                     # return self.current_state[y][x]
    #         verticalWinCount = 0
    #
    # def mainDiagCheck(self):
    #     # Main diagonal check
    #     checkX = 1
    #     checkY = 2
    #     mainDiagonalWinCount = 0
    #     for i in range(self.boardsize):
    #         if self.current_state[checkY][
    #             checkX] != '.' and checkX + 1 <= self.boardsize and checkY + 1 <= self.boardsize + 1 and self.current_state[checkY][checkX] == self.current_state[checkY + 1][checkX + 1]:
    #             mainDiagonalWinCount += 1
    #             print("main diagonal match found")
    #             if mainDiagonalWinCount + 1 == self.win_condition:
    #                 print(self.current_state[checkY][checkX], "Main diagonal win")
    #                 return True
    #                 # return self.current_state[checkY][checkX]
    #             checkX += i
    #             checkY += i
    #
    # def secDiagCheck(self):
    #     # Secondary diagonal check
    #     checkX = 1
    #     checkY = self.boardsize + 1
    #     secondaryDiagonalWinCount = 0
    #     for i in range(self.boardsize):
    #         if self.current_state[checkY][checkX] != '.' and checkX + 1 <= self.boardsize and checkY - 1 >= 0 and self.current_state[checkY][checkX] == self.current_state[checkY - 1][checkX + 1]:
    #             secondaryDiagonalWinCount += 1
    #             print("secondary diagonal match found")
    #             if secondaryDiagonalWinCount + 1 == self.win_condition:
    #                 print(self.current_state[checkY][checkX], "Secondary diagonal win")
    #                 return True
    #                 # return self.current_state[checkY][checkX]
    #             checkX += i
    #             checkY -= i
    #
    # def diagCheck(self):
    #     # diagonal check
    #     diagonalCheck = 0
    #     for y in range(self.boardsize + 2):
    #         for x in range(self.boardsize + 1):
    #             if self.current_state[y][x] == 'X' or self.current_state[y][x] == 'O':
    #                 for i in range(self.win_condition):
    #                     if x + i <= self.boardsize and y + i <= self.boardsize + 1 and (
    #                             self.current_state[y][x] == self.current_state[y + i][x + i] or self.current_state[y][x] == self.current_state[y - i][x - i]):
    #                         diagonalCheck += 1
    #                         print("diagonal match found")
    #                         if diagonalCheck == self.win_condition:
    #                             print(self.current_state[y][x], "diagonal win")
    #                             return True
    #                             # return self.current_state[y][x]
    #                     else:
    #                         break
    # def is_empty(self):
    #     # Check if empty
    #     for y in range(self.boardsize + 2):
    #         for x in range(self.boardsize + 1):
    #             if (self.current_state[y][x] == '.'):
    #                 return True
    #     # it's a tie
    #     return False

    def is_end(self):
        # Horizontal check
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if self.current_state[y][x] != '-' and self.current_state[y][x] != '.' and x + 1 <= self.boardsize and self.current_state[y][x] == self.current_state[y][x + 1]:
                    horizontalWinCount += 1
                    if horizontalWinCount + 1 == self.win_condition:
                        print(self.current_state[y][x], "Horizontal win")
                        return self.current_state[y][x]
            horizontalWinCount = 0

        # Vertical check
        for x in range(self.boardsize + 1):
            for y in range(self.boardsize + 2):
                if self.current_state[y][x] != '.' and y + 1 <= self.boardsize + 1 and self.current_state[y][x] == self.current_state[y + 1][x]:
                    verticalWinCount += 1
                    if verticalWinCount + 1 == self.win_condition:
                        print(self.current_state[y][x], "Vertical win")
                        return self.current_state[y][x]
            verticalWinCount = 0

        # Main diagonal check
        checkX = 1
        checkY = 2
        x = checkX
        y = checkY
        mainDiagonalWinCount = 0
        for i in range(self.boardsize):
            if self.current_state[checkY][
                checkX] != '.' and checkX + 1 <= self.boardsize and checkY + 1 <= self.boardsize + 1 and self.current_state[checkY][checkX] == self.current_state[y + 1][x + 1]:
                mainDiagonalWinCount += 1
                if mainDiagonalWinCount + 1 == self.win_condition:
                    print(self.current_state[checkY][checkX], "Main diagonal win")
                    return self.current_state[checkY][checkX]
                x += i
                y += i

        # Secondary diagonal check
        checkX = 1
        checkY = self.boardsize + 1
        x = checkX
        y = checkY
        secondaryDiagonalWinCount = 0
        for i in range(self.boardsize):
            if self.current_state[checkY][checkX] != '.' and x + 1 <= self.boardsize and y - 1 >= 0 and self.current_state[checkY][checkX] == self.current_state[y - 1][x + 1]:
                secondaryDiagonalWinCount += 1
                if secondaryDiagonalWinCount + 1 == self.win_condition:
                    print(self.current_state[checkY][checkX], "Secondary diagonal win")
                    return self.current_state[checkY][checkX]
                x += i
                y -= i

        # diagonal check
        diagonalCheck = 0
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if self.current_state[y][x] == 'X' or self.current_state[y][x] == 'O':
                    checkX = x
                    checkY = y
                    for i in range(self.win_condition):
                        if x + i <= self.boardsize and y + i <= self.boardsize + 1 and (
                                self.current_state[checkY][checkX] == self.current_state[y + i][x + i] or self.current_state[checkY][checkX] == self.current_state[y - i][x - i]):
                            diagonalCheck += 1
                            if diagonalCheck == self.win_condition:
                                print(self.current_state[y][x], "diagonal win")
                                return self.current_state[y][x]
                        else:
                            diagonalCheck = 0
                            return None

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
        return self.result

    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    def minimax(self, max=False, totalTime=0):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 2 or -2 as worse than the worst case:
        start = time.time()
        value = 2
        if max:
            value = -2
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return (-1, x, y)
        elif result == 'O':
            return (1, x, y)
        elif result == '.':
            return (0, x, y)
        for i in range(self.boardsize):
            for j in range(self.boardsize):
                curr = time.time() - start
                if curr <= totalTime:
                    if self.current_state[i][j] == '.':
                        if max:
                            self.current_state[i][j] = 'O'
                            (v, _, _) = self.minimax(max=False)
                            if v > value:
                                value = v
                                x = i
                                y = j
                        else:
                            self.current_state[i][j] = 'X'
                            (v, _, _) = self.minimax(max=True)
                            if v < value:
                                value = v
                                x = i
                                y = j
                        self.current_state[i][j] = '.'
                # else:
                #     return (value, x, y)
        return (value, x, y)

    def alphabeta(self, alpha=-2, beta=2, max=False, totalTime=0):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 2 or -2 as worse than the worst case:
        start = time.time()
        value = 2
        if max:
            value = -2
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return (-1, x, y)
        elif result == 'O':
            return (1, x, y)
        elif result == '.':
            return (0, x, y)
        for i in range(self.boardsize):
            for j in range(self.boardsize):
                curr = time.time() - start
                if curr <= totalTime:
                    if self.current_state[i][j] == '.':
                        if max:
                            self.current_state[i][j] = 'O'
                            (v, _, _) = self.alphabeta(alpha, beta, max=False)
                            if v > value:
                                value = v
                                x = i
                                y = j
                        else:
                            self.current_state[i][j] = 'X'
                            (v, _, _) = self.alphabeta(alpha, beta, max=True)
                            if v < value:
                                value = v
                                x = i
                                y = j
                        self.current_state[i][j] = '.'
                        if max:
                            if value >= beta:
                                return (value, x, y)
                            if value > alpha:
                                alpha = value
                        else:
                            if value <= alpha:
                                return (value, x, y)
                            if value < beta:
                                beta = value
                else:
                    return (value, x, y)
        return (value, x, y)

    def play(self, algo=None,player_x=None,player_o=None, t=0):
        if algo == None or algo == False:
            algo = self.ALPHABETA
        if algo == True:
            algo = self.MINIMAX
        if player_x == None:
            player_x = self.HUMAN
        if player_o == None:
            player_o = self.HUMAN

        while True:
            self.draw_board()
            if self.check_end():
                print("Winner is found")
                return
            # self.player_input()

            start = time.time()
            if algo == self.MINIMAX:
                if self.player_turn == 'X':
                    (_, x, y) = self.minimax(max=False, totalTime=t)
                else:
                    (_, x, y) = self.minimax(max=True, totalTime=t)
            else:  # algo == self.ALPHABETA
                if self.player_turn == 'X':
                    (m, x, y) = self.alphabeta(max=False, totalTime=t)
                else:
                    (m, x, y) = self.alphabeta(max=True, totalTime=t)
            end = time.time()

            if (self.player_turn == 'X' and player_x == self.HUMAN) or (
                    self.player_turn == 'O' and player_o == self.HUMAN):
                (x, y) = self.player_input()
            if (self.player_turn == 'X' and player_x == self.AI) or (self.player_turn == 'O' and player_o == self.AI):
                print(F'Evaluation time: {round(end - start, 7)}s')
                print(F'Player {self.player_turn} under AI control plays: x = {x-2}, y = {self.LETTERS[y-1]}')
            self.current_state[x][y] = self.player_turn
            print(self.current_state)
            self.switch_player()

#boardsize=n, nbrOfBlocs=b, win_condition=s, totalTime=t
# def trace(cmd, n, b, s, t):
#     with open('output/gameTrace-' + n + '' + b + ''s + '' + t + '.txt', 'w+', encoding='utf-8') as gameTrace:
#         os.system(cmd)

def main():
    while True:
        try:
            mode = int(input('Would you like (X, O):\n1. HUMAN vs HUMAN \n2. HUMAN vs AI \n3. AI vs HUMAN \n4. AI vs AI\n'))
        except ValueError:
                print("Invalid Input.\n")
                continue
        else:
            if 1 <= mode <= 4:
                break
            else:
                print("Invalid Input.\n")
                continue
    algorithm = False
    while mode != 1:
        try:
            algoChoice = int(input('Which algorithm?\n1. MINIMAX \n2. ALPHABETA\n'))
        except ValueError:
                print("Invalid Input.\n")
                continue
        else:
            if 1 <= algoChoice <= 2:
                if algoChoice == 1:
                    algorithm == True # ALPHABETA
                elif algoChoice == 2:
                    algorithm == False # MINIMAX
                break
            else:
                print("Invalid Input")
                continue

    userTime = 0
    while True:
        try:
            userTime = int(input('What is the time constraint (1 - 5 seconds)?\n'))
        except ValueError:
                print("Invalid Input.\n")
                continue
        else:
            if 1 <= userTime <= 5:
                break
            else:
                print("Invalid Input")
                continue

    g = Game()
    if mode == 1:
        g.play(algo=Game.ALPHABETA,player_x=Game.HUMAN,player_o=Game.HUMAN, t=userTime)
        # g.trace()
    elif mode == 2:
        g.play(algo=Game.MINIMAX,player_x=Game.HUMAN,player_o=Game.AI, t=userTime)
    elif mode == 3:
        g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN, t=userTime)
    elif mode == 4:
        g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.AI, t=userTime)
    else:
        exit()
if __name__ == "__main__":
    main()
