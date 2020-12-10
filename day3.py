import comm

print('start!')

testFilePath = 'day3.txt'

lines = comm.readFileToList(testFilePath)

mapH = len(lines)
mapW = len(lines[0].replace('\n', ''))
print(f'mapH: {mapH}, mapW: {mapW}')

result = 0
x = 0
y = 0
step = 3

for index, line in enumerate(lines):
    if index != y:
        listLine = list(line.replace('\n', ''))
        
        x += step
        if x > mapW - 1:
            x = x - mapW
        
        print(listLine, f' x: {x}, {listLine[x]}')
        
        if (listLine[x] == '#'): result += 1
        

print(result)

print('done...')