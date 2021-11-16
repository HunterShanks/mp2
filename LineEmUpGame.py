import time
from random import randrange

class Game:
    # Constants initialized
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self):
        self.initialize_game()

    # Initializes the game for the game state
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
                    BOARDSIZE = self.boardsize
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
                    NBROFBLOCS = self.nbrOfBlocs
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
                    WINCONDITION = self.win_condition
                    break
                else:
                    print("Invalid Input.")
                    continue

        # Generating Blocs
        # FOR GAMETRACE 4435 AND 4431
        # blocXIndex = [0, 0, 4, 4]
        # blockYIndex = [0, 4, 0, 4]

        self.blocXIndex = []
        self.blocYIndex = []
        for i in range(self.nbrOfBlocs):
            bloc_coordinate_x = randrange(self.boardsize)
            bloc_coordinate_y = randrange(self.boardsize)
            self.blocXIndex.append(bloc_coordinate_x)
            self.blocYIndex.append(bloc_coordinate_y)

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
                    if self.blocXIndex[i] == x and self.blocYIndex[i] == y:
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

    # Validates the the input move from HUMAN or AI
    def is_valid(self, px, py):
        if px < 0 or px > self.boardsize+1 or py < 0 or py > self.boardsize:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    # Function for the player (HUMAN or AI) inputs
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

    # Draws the board on screen
    def draw_board(self):
        print()
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                print(F'{self.current_state[y][x]}', end="")
            print()
        print()

    # Checks each direction for a win, the diagonal check works partially
    def is_end(self):
        # Horizontal check
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if self.current_state[y][x] != '-' and self.current_state[y][x] != '.' and x + 1 <= self.boardsize and \
                        self.current_state[y][x] == self.current_state[y][x + 1]:
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

        # Diagonal check
        mainDiagonalWinCheck = 0
        secondaryDiagonalWinCheck = 0
        for y in range(self.boardsize + 2):
            for x in range(self.boardsize + 1):
                if self.current_state[y][x] == 'X' or self.current_state[y][x] == 'O':
                    for i in range(self.win_condition):
                        if x + i <= self.boardsize and y + i <= self.boardsize + 1 and self.current_state[y][
                            x] == self.current_state[y + i][x + i]:
                            mainDiagonalWinCheck += 1
                            if mainDiagonalWinCheck == self.win_condition:
                                return self.current_state[y][x]
                        elif x == self.boardsize and self.current_state[y][x] == self.current_state[y - 1][
                            x - 1]:
                            mainDiagonalWinCheck += 1
                            if mainDiagonalWinCheck == self.win_condition:
                                return self.current_state[y][x]
                        if x - i >= 1 and y + i <= self.boardsize + 1 and self.current_state[y][x] == \
                                self.current_state[y + i][x - i]:
                            secondaryDiagonalWinCheck += 1
                            if secondaryDiagonalWinCheck == self.win_condition:
                                return self.current_state[y][x]
                        elif x == 1 and y >= 2 and self.current_state[y][x] == self.current_state[y - 1][x + 1]:
                            secondaryDiagonalWinCheck += 1
                            if secondaryDiagonalWinCheck == self.win_condition:
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

    # Validates the win condition
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

    # Changes player turn
    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    # MINIMAX function
    def minimax(self, max=False, totalTime=0):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 2 or -2 as worse than the worst case

        # Initializes variables
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
        return (value, x, y)

    def alphabeta(self, alpha=-2, beta=2, max=False, totalTime=0):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 2 or -2 as worse than the worst case

        # Initializes variables
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

    # Playing the game
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


    # Getters -------------------------------------------------------------------------
    def getBoardSize(self):
        return self.boardsize

    def getXindex(self):
        return self.blocXIndex

    def getYindex(self):
        return self.blocYIndex

    def getBoardSize(self):
        return self.boardsize

    def getXindex(self, i):
        return self.blocXIndex[i]

    def getYindex(self, i):
        return self.blocYIndex[i]

    def getNbrBlocs(self):
        return self.nbrOfBlocs

    def getWinCond(self):
        return self.win_condition

    def getNbrBlocs(self):
        return self.nbrOfBlocs

    def getWinCond(self):
        return self.win_condition

    def getCurrState(self):
        return self.current_state

# Main -------------------------------------------------------------------------
def main():
    # User input with validation
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

    # For each mode, we play the game then print the final output to the gameTrace file
    # Due to the implementation, we were unable to print for every move
    if mode == 1:
        g.play(algo=Game.ALPHABETA,player_x=Game.HUMAN,player_o=Game.HUMAN, t=userTime)
        with open('output/gameTrace-' + str(g.getBoardSize()) + str(g.getNbrBlocs()) + str(g.getWinCond()) + str(userTime) + '.txt', 'w+', encoding='utf-8') as gameTrace:
            gameTrace.write('n=' + str(g.getBoardSize()) + ' b=' + str(g.getNbrBlocs()) + ' s=' + str(g.getWinCond()) + ' t=' + str(userTime) + '\n')

            blocIndices = []
            for i in range(g.getNbrBlocs()):
                blocIndices.append('(' + str(g.getXindex(i)) + ',' + str(g.getYindex(i)) + ')')

            gameTrace.write(f'blocs={blocIndices}\n\n')

            stateCopy = g.getCurrState()
            for i in range(len(stateCopy)):
                gameTrace.write(str(stateCopy[i]) + '\n')

            gameTrace.write(f'i Evaluation time: {str(g.getEvalTime())}')


    elif mode == 2:
        g.play(algo=Game.MINIMAX,player_x=Game.HUMAN,player_o=Game.AI, t=userTime)
        with open('output/gameTrace-' + str(g.getBoardSize()) + str(g.getNbrBlocs()) + str(g.getWinCond()) + str(userTime) + '.txt', 'w+', encoding='utf-8') as gameTrace:
            gameTrace.write('n=' + str(g.getBoardSize()) + ' b=' + str(g.getNbrBlocs()) + ' s=' + str(g.getWinCond()) + ' t=' + str(userTime) + '\n')

            blocIndices = []
            for i in range(g.getNbrBlocs()):
                blocIndices.append('(' + str(g.getXindex(i)) + ',' + str(g.getYindex(i)) + ')')

            gameTrace.write(f'blocs={blocIndices}\n\n')

            stateCopy = g.getCurrState()
            for i in range(len(stateCopy)):
                gameTrace.write(str(stateCopy[i]) + '\n')

            gameTrace.write(f'i Evaluation time: {str(g.getEvalTime())}')


    elif mode == 3:
        g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN, t=userTime)
        with open('output/gameTrace-' + str(g.getBoardSize()) + str(g.getNbrBlocs()) + str(g.getWinCond()) + str(userTime) + '.txt', 'w+', encoding='utf-8') as gameTrace:
            gameTrace.write('n=' + str(g.getBoardSize()) + ' b=' + str(g.getNbrBlocs()) + ' s=' + str(g.getWinCond()) + ' t=' + str(userTime) + '\n')

            blocIndices = []
            for i in range(g.getNbrBlocs()):
                blocIndices.append('(' + str(g.getXindex(i)) + ',' + str(g.getYindex(i)) + ')')

            gameTrace.write(f'blocs={blocIndices}\n\n')

            stateCopy = g.getCurrState()
            for i in range(len(stateCopy)):
                gameTrace.write(str(stateCopy[i]) + '\n')

            gameTrace.write(f'i Evaluation time: {str(g.getEvalTime())}')

    elif mode == 4:
        g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.AI, t=userTime)
        with open('output/gameTrace-' + str(g.getBoardSize()) + str(g.getNbrBlocs()) + str(g.getWinCond()) + str(userTime) + '.txt', 'w+', encoding='utf-8') as gameTrace:
            gameTrace.write('n=' + str(g.getBoardSize()) + ' b=' + str(g.getNbrBlocs()) + ' s=' + str(g.getWinCond()) + ' t=' + str(userTime) + '\n')

            blocIndices = []
            for i in range(g.getNbrBlocs()):
                blocIndices.append('(' + str(g.getXindex(i)) + ',' + str(g.getYindex(i)) + ')')

            gameTrace.write(f'blocs={blocIndices}\n\n')

            stateCopy = g.getCurrState()
            for i in range(len(stateCopy)):
                gameTrace.write(str(stateCopy[i]) + '\n')

            gameTrace.write(f'i Evaluation time: {str(g.getEvalTime())}')

    else:
        exit()

if __name__ == "__main__":
    main()
