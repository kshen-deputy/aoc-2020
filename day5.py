import comm

print('start!')

testFilePath = 'day5.txt'

lines = comm.readFileToList(testFilePath)

print(list(lines[0]))

result = 0

def binarySearch(rowCode, l, h):
    for code in rowCode:
        if code == 'F' or code == 'L':
            m = (l + h - 1) / 2
            h = m
        else:
            m = (l + h + 1) / 2
            l = m
    return l

def calcRow(rowCode):
    row = binarySearch(rowCode, 0, 127)
    print(f'rowCode: {rowCode}, find row: {row}')
    return row

def calcColumn(columnCode):
    column = binarySearch(columnCode, 0, 7)
    print(f'column: {columnCode}, find: {column}')
    return column

def calcSeatID(code):
    codeList = list(code)
    row = calcRow(codeList[0:7])
    column = calcColumn(codeList[7:])
    seatID = row * 8 + column
    return seatID

for line in lines:
    line = line.replace('\n', '')
    seatID = calcSeatID(line)
    if seatID > result: result = seatID

print(result)

print('done...')