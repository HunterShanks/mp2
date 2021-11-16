import time
import drawBoardTest
from random import randrange

# Use for second heuristic
# def getBestNeighbour(self, neighbours):
#     bestRouteLength = routeLength(self, neighbours[0])
#     bestNeighbour = neighbours[0]
#     for neighbour in neighbours:
#         currentRouteLength = routeLength(self, neighbour)
#         if currentRouteLength < bestRouteLength:
#             bestRouteLength = currentRouteLength
#             bestNeighbour = neighbour
#     return bestNeighbour, bestRouteLength

# def hillClimbing(self):
#     currentSolution = randomSolution(self)
#     # currentRouteLength = routeLength(self, currentSolution)
#     neighbours = getNeighbours(currentSolution)
#     bestNeighbour = getBestNeighbour(self, neighbours)
#
#     while bestNeighbourRouteLength < currentRouteLength:
#         currentSolution = bestNeighbour
#         currentRouteLength = bestNeighbourRouteLength
#         neighbours = getNeighbours(currentSolution)
#         bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(self, neighbours)
#
#     return currentSolution, currentRouteLength

#---------------------------------------------------------------------------------------------------------------------------
# heuristic e1 -> fast one
#---------------------------------------------------------------------------------------------------------------------------
heuValue = 0
countX, countO = 0, 0

start_time = time.time()
for all rows, cols in range (drawBoardTest.current_state) do:
    if drawBoardTest.current_state contains drawBoardTest.win_condition:
        heuValue += 1000
    elif drawBoardTest.current_state contains -drawBoardTest.win_condition:
        heuValue -= 1000


    if drawBoardTest.current_state[col][row] == 'X':
        countX -= 10
    elif drawBoardTest.current_state[col][row] == 'O':
        countO += 10

return heuValue

# horizontal() -> if open spot, put(X)
for x in range(drawBoardTest.boardsize + 1):
    for y in range(drawBoardTest.boardsize + 2):
        if current_state[y][x] != '.' and y + 1 <= drawBoardTest.boardsize + 1 and drawBoardTest.current_state[y][x] == drawBoardTest.current_state[y + 1][x]:
            neighbourCount += 1

            # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
            if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                # If next spot is empty -> place yourself in that spot
                if current_state[y + 2][x] == '.':
                    drawBoardTest.current_state[y + 2][x] == drawBoardTest.current_state[y][x]
                    endTurn = True
                else:
                    x = drawBoardTest.boardsize + 1
                    break
            # if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:
            #     print(current_state[y][x], "vertical win")
            #     break
    neighbourCount = 0

# Looping through all possible placements
if endTurn == False:
    rand = 2
elif rand == 2
# horizontal() -> if open spot, put(X)
for y in range(drawBoardTest.boardsize + 2):
    for x in range(drawBoardTest.boardsize + 1):
        if drawBoardTest.current_state[y][x] != '-' and drawBoardTest.current_state[y][x] != '.' and x + 1 <= drawBoardTest.boardsize and drawBoardTest.current_state[y][x] == drawBoardTest.current_state[y][x + 1]:
            neighbourCount += 1

            # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
            if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                # If next spot is empty -> place yourself in that spot
                if drawBoardTest.current_state[y][x + 2] == '.':
                    drawBoardTest.current_state[y][x + 2] == drawBoardTest.current_state[y][x]
                    endTurn = True
                else:
                    y = drawBoardTest.boardsize + 1
                    break
            # if neighbourCount + 1 == drawBoardTest.win_condition:
            #     print(current_state[y][x], "horizontal win")  # change to return in skeleton
            #     break
    neighbourCount = 0

# Looping through all possible placements
if endTurn == False:
    rand = 3
elif rand == 3
# diag() -> if open spot, put(X)
# Main diagonal check
checkX = 1
checkY = 2
for i in range(drawBoardTest.boardsize):
    if drawBoardTest.current_state[checkY][checkX] != '.' and checkX + 1 <= drawBoardTest.boardsize and checkY + 1 <= drawBoardTest.boardsize + 1 and drawBoardTest.current_state[checkY][checkX] == drawBoardTest.current_state[checkY + 1][checkX + 1]:
        neighbourCount += 1

        # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
        if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

            # If next spot is empty -> place yourself in that spot
            if drawBoardTest.current_state[checkY + 2][checkX + 2] == '.':
                drawBoardTest.current_state[checkY + 2][checkX + 2] == drawBoardTest.current_state[y][x]
                endTurn = True
            else:
                i = drawBoardTest.boardsize
                break
        # if neighbourCount + 1 == drawBoardTest.win_condition:
        #     print(current_state[checkY][checkX], "Main diagonal win")
        #     break
        checkX += i
        checkY += i

    neighbourCount = 0

# Secondary diagonal check
checkX = 1
checkY = drawBoardTest.boardsize + 1
for i in range(drawBoardTest.boardsize):
    if drawBoardTest.current_state[checkY][checkX] != '.' and checkX + 1 <= drawBoardTest.boardsize and checkY - 1 >= 0 and drawBoardTest.current_state[checkY][checkX] == drawBoardTest.current_state[checkY - 1][checkX + 1]:
        neighbourCount += 1

        # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
        if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

            # If next spot is empty -> place yourself in that spot
            if drawBoardTest.current_state[checkY - 1][checkX + 1] == '.':
                drawBoardTest.current_state[checkY - 1][checkX + 1] == drawBoardTest.current_state[y][x]
                endTurn = True
            else:
                i = drawBoardTest.boardsize
                break
        # if neighbourCount + 1 == drawBoardTest.win_condition:
        #     print(current_state[checkY][checkX], "Secondary diagonal win")
        #     break
        checkX += i
        checkY -= i

    neighbourCount = 0

# diagonal check
for y in range(drawBoardTest.boardsize + 2):
    for x in range(drawBoardTest.boardsize + 1):
        if drawBoardTest.current_state[y][x] == 'X' or drawBoardTest.current_state[y][x] == 'O':
            for i in range(drawBoardTest.win_condition):
                if x + i <= drawBoardTest.boardsize and y + i <= drawBoardTest.boardsize + 1 and (drawBoardTest.current_state[y][x] == drawBoardTest.current_state[y+i][x+i] or drawBoardTest.current_state[y][x] == current_state[y-i][x-i]):
                    neighbourCount += 1

                    # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
                    if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                        # If next spot is empty -> place yourself in that spot
                        if current_state[y+i][x+i] == '.':
                            drawBoardTest.current_state[y][x + 2] == drawBoardTest.current_state[y][x]
                            endTurn = True
                        elif drawBoardTest.current_state[y-i][x-i] = '.':
                            drawBoardTest.current_state[y][x + 2] == drawBoardTest.current_state[y][x]
                            endTurn = True
                        else:
                            y = drawBoardTest.boardsize + 2
                            break
                    # if neighbourCount == drawBoardTest.win_condition:
                    #     print(current_state[y][x], "diagonal win")
                    #     break

    neighbourCount = 0

# Looping through all possible placements
if endTurn == False:
    rand = 1

start_time = time.time()


#---------------------------------------------------------------------------------------------------------------------------
# heuristic e2
#---------------------------------------------------------------------------------------------------------------------------
# Initializing the heuValue
heuValue = drawBoardTest.boardsize * drawBoardTest.boardsize

# horizontal check if its empty:
for y in range(drawBoardTest.boardsize + 2):
    for x in range(drawBoardTest.boardsize + 1):
        newHeuValue = -1

        drawBoardTest.current_state[y][x]

def somefunc():
    for y in range (drawBoardTest.boardsize):
        for x in range(drawBoardTest.boardsize):
            #boardValue[y][x] = -1????

            # Uses the index of y and x to verify that both are placed in the same spot
            if index(boardValue[y][x]) == index(drawBoardTest.current_state[y][x]):
                boardValue[y][x] = -2
                return something
#
# call skeleton-tictactoe.switch_player() -> not needed because we need to simply decide on a move,
# and the next turn will flip within the tictactoe file automatically within the play function.
# Check the def of play, just put the heuristic function in the algo and add if statement
# if algo == heuristic function then call the function itself with the appropriate params
#
# Returns neighbours
def getNeighbours(self):
    vertical = 1
    horizontal = 2
    diag = 3
    neighbourCount = 0
    rand = randrange(1 ,3)
    endTurn = False

    if rand == 1
        # vertical() -> if neighbour == yourself, check if next spot open, put(X)
        for x in range(drawBoardTest.boardsize + 1):
            for y in range(drawBoardTest.boardsize + 2):
                if current_state[y][x] != '.' and y + 1 <= drawBoardTest.boardsize + 1 and drawBoardTest.current_state[y][x] == drawBoardTest.current_state[y + 1][x]:
                    neighbourCount += 1

                    # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
                    if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                        # If next spot is empty -> place yourself in that spot
                        if current_state[y + 2][x] == '.':
                            drawBoardTest.current_state[y + 2][x] == drawBoardTest.current_state[y][x]
                            endTurn = True
                        else:
                            x = drawBoardTest.boardsize + 1
                            break
                    # if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:
                    #     print(current_state[y][x], "vertical win")
                    #     break
            neighbourCount = 0

        # Looping through all possible placements
        if endTurn == False:
            rand = 2
    elif rand == 2
        # horizontal() -> if open spot, put(X)
        for y in range(drawBoardTest.boardsize + 2):
            for x in range(drawBoardTest.boardsize + 1):
                if drawBoardTest.current_state[y][x] != '-' and drawBoardTest.current_state[y][x] != '.' and x + 1 <= drawBoardTest.boardsize and drawBoardTest.current_state[y][x] == drawBoardTest.current_state[y][x + 1]:
                    neighbourCount += 1

                    # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
                    if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                        # If next spot is empty -> place yourself in that spot
                        if drawBoardTest.current_state[y][x + 2] == '.':
                            drawBoardTest.current_state[y][x + 2] == drawBoardTest.current_state[y][x]
                            endTurn = True
                        else:
                            y = drawBoardTest.boardsize + 1
                            break
                    # if neighbourCount + 1 == drawBoardTest.win_condition:
                    #     print(current_state[y][x], "horizontal win")  # change to return in skeleton
                    #     break
            neighbourCount = 0

        # Looping through all possible placements
        if endTurn == False:
            rand = 3
    elif rand == 3
        # diag() -> if open spot, put(X)
        # Main diagonal check
        checkX = 1
        checkY = 2
        for i in range(drawBoardTest.boardsize):
            if drawBoardTest.current_state[checkY][checkX] != '.' and checkX + 1 <= drawBoardTest.boardsize and checkY + 1 <= drawBoardTest.boardsize + 1 and drawBoardTest.current_state[checkY][checkX] == drawBoardTest.current_state[checkY + 1][checkX + 1]:
                neighbourCount += 1

                # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
                if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                    # If next spot is empty -> place yourself in that spot
                    if drawBoardTest.current_state[checkY + 2][checkX + 2] == '.':
                        drawBoardTest.current_state[checkY + 2][checkX + 2] == drawBoardTest.current_state[y][x]
                        endTurn = True
                    else:
                        i = drawBoardTest.boardsize
                        break
                # if neighbourCount + 1 == drawBoardTest.win_condition:
                #     print(current_state[checkY][checkX], "Main diagonal win")
                #     break
                checkX += i
                checkY += i

            neighbourCount = 0

        # Secondary diagonal check
        checkX = 1
        checkY = drawBoardTest.boardsize + 1
        for i in range(drawBoardTest.boardsize):
            if drawBoardTest.current_state[checkY][checkX] != '.' and checkX + 1 <= drawBoardTest.boardsize and checkY - 1 >= 0 and drawBoardTest.current_state[checkY][checkX] == drawBoardTest.current_state[checkY - 1][checkX + 1]:
                neighbourCount += 1

                # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
                if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                    # If next spot is empty -> place yourself in that spot
                    if drawBoardTest.current_state[checkY - 1][checkX + 1] == '.':
                        drawBoardTest.current_state[checkY - 1][checkX + 1] == drawBoardTest.current_state[y][x]
                        endTurn = True
                    else:
                        i = drawBoardTest.boardsize
                        break
                # if neighbourCount + 1 == drawBoardTest.win_condition:
                #     print(current_state[checkY][checkX], "Secondary diagonal win")
                #     break
                checkX += i
                checkY -= i

            neighbourCount = 0

        # diagonal check
        for y in range(drawBoardTest.boardsize + 2):
            for x in range(drawBoardTest.boardsize + 1):
                if drawBoardTest.current_state[y][x] == 'X' or drawBoardTest.current_state[y][x] == 'O':
                    for i in range(drawBoardTest.win_condition):
                        if x + i <= drawBoardTest.boardsize and y + i <= drawBoardTest.boardsize + 1 and (drawBoardTest.current_state[y][x] == drawBoardTest.current_state[y+i][x+i] or drawBoardTest.current_state[y][x] == current_state[y-i][x-i]):
                            neighbourCount += 1

                            # Checks if theres more than 0 neighbours for a more favorable outcome ie closer to winning
                            if neighbourCount > 0 and neighbourCount <= drawBoardTest.win_condition:

                                # If next spot is empty -> place yourself in that spot
                                if current_state[y+i][x+i] == '.':
                                    drawBoardTest.current_state[y][x + 2] == drawBoardTest.current_state[y][x]
                                    endTurn = True
                                elif drawBoardTest.current_state[y-i][x-i] = '.':
                                    drawBoardTest.current_state[y][x + 2] == drawBoardTest.current_state[y][x]
                                    endTurn = True
                                else:
                                    y = drawBoardTest.boardsize + 2
                                    break
                            # if neighbourCount == drawBoardTest.win_condition:
                            #     print(current_state[y][x], "diagonal win")
                            #     break

            neighbourCount = 0

        # Looping through all possible placements
        if endTurn == False:
            rand = 1
    else:
        # N o neighbour found -> board full
        skeleton-tictactoe.check_end()
