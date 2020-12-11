import comm

print('start!')

testFilePath = 'day11.txt'

lines = comm.readFileToList(testFilePath)

seats = []
for line in lines:
    line = line.replace('\n', '')
    seats.append(list(line))

rowLen = len(seats[0])
columnLen = len(seats)

def getAdjSeatByDirection(seats, rowId, columnId, rowOffset, columnOffset):
    rowAdj = rowId + rowOffset
    columnAdj = columnId + columnOffset
    while rowAdj >= 0 and rowAdj <= columnLen - 1 and columnAdj >= 0 and columnAdj <= rowLen - 1:
        adj = seats[rowAdj][columnAdj]
        if adj == '.':
            rowAdj += rowOffset
            columnAdj += columnOffset
        elif adj == 'L':
            return 0
        else:
            return 1
    return 0

def getAdjacent(seats, rowId, columnId):
    total = 0
    # ok let's do eight directions
    for rowOffset in range(-1,2):
        for columnOffset in range(-1,2):
            if rowOffset == 0 and columnOffset == 0:
                # print('ignore itself')
                ''
            else:
                total += getAdjSeatByDirection(seats, rowId, columnId, rowOffset, columnOffset)
    # print(f'getAdjacent: {total}')
    return total

def processSeat(seat, seats, rowId, columnId):
    res = ''
    if seat == 'L' and getAdjacent(seats, rowId, columnId) == 0:
        res = '#'
    elif seat == '#' and getAdjacent(seats, rowId, columnId) >= 5:
        res = 'L'
    elif seat == '.':
        res = '.'
    else:
        res = seat
    # print(f'r, c: {rowId}, {columnId}, new seat {res}')
    return res

def takeSeats(seats):
    newSeats = []
    for rowId in range(columnLen):
        newRow = []
        for columnId in range(rowLen):
            curSeat = seats[rowId][columnId]
            newSeat = processSeat(curSeat, seats, rowId, columnId)
            newRow.append(newSeat)
        newSeats.append(newRow)
    return newSeats

while True:
    newSeats = takeSeats(seats)
    if newSeats == seats:
        break
    else:
        seats = newSeats
    
result = 0
for row in seats:
    for seat in row:
        if seat == '#': result+=1

print(result)
print('done...')
