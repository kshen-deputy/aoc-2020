import comm

print('start!')

testFilePath = 'day5.txt'

lines = comm.readFileToList(testFilePath)

print(list(lines[0]))

result = 0
resultList = []

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
    seatID = int(calcSeatID(line))
    # if seatID > result: result = seatID
    resultList.append(seatID)

def findMissingNumber(r):
    r.sort()
    print(r)
    s = len(r)
    l = 0
    h = s - 1
    while h - l > 1:
        m = int((l + h) / 2)
        print(f'middle index: {m}, middle number: {r[m]}, compare to: {int((r[l] + r[h] - 1) / 2)}')
        if r[m] == int((r[l] + r[h] - 1) / 2):
            l = m
        else:
            h = m
    print(f'l: {l}, h: {h}')
    return r[l]

result = findMissingNumber(resultList)
print(result + 1)

print('done...')