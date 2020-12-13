import comm

print('start!')

testFilePath = 'day12.txt'

lines = comm.readFileToList(testFilePath)

directions = ['E', 'S', 'W', 'N']
curP = [0, 0]
curD = 'E'

def move(d, p, u):
    if d == 'E': p[0] = p[0] + u
    elif d == 'W': p[0] = p[0] - u
    elif d == 'N': p[1] = p[1] + u
    else: p[1] = p[1] - u
    return p

for line in lines:
    line = line.replace('\n', '')
    d = line[:1]
    unit = int(line[1:])
    print(f'd: {d} unit: {unit} cur: {curD}')
    if d == 'F':
        curP = move(curD, curP, unit)
    elif d == 'L':
        offset = unit / 90
        newDirectionIndex = directions.index(curD) - offset
        newDirectionIndex = newDirectionIndex + 4 if newDirectionIndex < 0 else newDirectionIndex
        curD = directions[int(newDirectionIndex)]
    elif d == 'R':
        offset = unit / 90
        newDirectionIndex = directions.index(curD) + offset
        newDirectionIndex = newDirectionIndex - 4 if newDirectionIndex > 3 else newDirectionIndex
        curD = directions[int(newDirectionIndex)]
    else:
        curP = move(d, curP, unit)

print(f'after all movements: {curP}')
print(f'result is: {abs(curP[0]) + abs(curP[1])}')
print('done...')
