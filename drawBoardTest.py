from random import randrange

letterAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
            print("Invalid Input. Too many blocs")
            continue

    # FOR GAMETRACE 4435 AND 4431
    # blocXIndex = [0, 0, 4, 4]
    # blockYIndex = [0, 4, 0, 4]

print("Generating bloc coordinates.")
blocXIndex = []
blocYIndex = []
for i in range(nbrOfBlocs):
    bloc_coordinate_x = randrange(nbrOfBlocs)
    bloc_coordinate_y = randrange(nbrOfBlocs)
    blocXIndex.append(bloc_coordinate_x)
    blocYIndex.append(bloc_coordinate_y)
    print(letterAxis[blocXIndex[i]], blocYIndex[i])




current_state = []
separator = [' +']
letterSep = ['  ']
for i in range(boardsize):
    letterSep.append(letterAxis[i])
    separator.append('-')
current_state.append(letterSep)
current_state.append(separator)

bloc_placed = False
for y in range(boardsize):
    row = [str(y) + '|']
    for x in range(boardsize):
        for i in range(nbrOfBlocs):
            if blocXIndex[i] == x and blocYIndex == y:
                row.append('*')
                bloc_placed = True
                break
        if bloc_placed:
            bloc_placed = False
            break
        else:
            row.append('.')
    current_state.append(row)

print(current_state)

print("Drawing Board")
print()
for x in range(boardsize):
    for y in range(boardsize):
        print(F'{current_state[x][y]}', end="")
    print()
print()
