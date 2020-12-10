import comm

print('start!')

testFilePath = 'day3.txt'

lines = comm.readFileToList(testFilePath)

mapH = len(lines)
mapW = len(lines[0].replace('\n', ''))
print(f'mapH: {mapH}, mapW: {mapW}')

resultList = []
result = 1

slopes = [
    {'xStep': 1, 'yStep': 1},
    {'xStep': 3, 'yStep': 1},
    {'xStep': 5, 'yStep': 1},
    {'xStep': 7, 'yStep': 1},
    {'xStep': 1, 'yStep': 2}
]
        
def getTrees(x, y, xStep, yStep):
    res = 0
    y += yStep

    while (y < mapH):
        listLine = list(lines[y].replace('\n', ''))

        x += xStep

        if x > mapW - 1: x -= mapW

        print(listLine, f' x: {x}, {listLine[x]}')

        if (listLine[x] == '#'): res += 1

        y += yStep

    return res

for slope in slopes:
    xStep = slope['xStep']
    yStep = slope['yStep']
    res = getTrees(0, 0, xStep, yStep)
    resultList.append(res)

print(resultList)

for n in resultList:
    result *= n

print(result)

print('done...')