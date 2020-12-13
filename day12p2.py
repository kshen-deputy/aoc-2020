import comm

print('start!')

testFilePath = 'day12.txt'

lines = comm.readFileToList(testFilePath)

curP = [0, 0]
wayP = [10, 1]

def moveWayPoint(wp, d, unit):
    if d == 'E': wp[0] = wp[0] + unit
    elif d == 'W': wp[0] = wp[0] - unit
    elif d == 'N': wp[1] = wp[1] + unit
    else: wp[1] = wp[1] - unit
    return wp

# rotates the waypoint clockwise around the ship clockwise 90 * offset degrees
# ship always facing East
def rotateWayPoint(wp, d, unit):
    offset = unit / 90 # 1, 2, 3
    if d == 'R':
        if offset == 1:
            res = [wp[1], wp[0] * -1]
        elif offset == 2:
            res = [wp[0] * -1, wp[1] * -1]
        else:
            res = [wp[1] * -1, wp[0]]
    else:
        if offset == 1:
            res = [wp[1] * -1, wp[0]]
        elif offset == 2:
            res = [wp[0] * -1, wp[1] * -1]
        else:
            res = [wp[1], wp[0] * -1]
    return res

# move forward to the waypoint a number of times equal to the given value
def move(wp, p, t):
    return [p[0] + wp[0] * t, p[1] + wp[1] * t]

for line in lines:
    line = line.replace('\n', '')
    d = line[:1]
    unit = int(line[1:])
    print(f'd: {d} unit: {unit} way point: {wayP}')
    if d == 'F':
        curP = move(wayP, curP, unit)
    elif d == 'L' or d == 'R':
        wayP = rotateWayPoint(wayP, d, unit)
    else: # E S W N
        wayP = moveWayPoint(wayP, d, unit)

print(f'after all movements: {curP}')
print(f'result is: {abs(curP[0]) + abs(curP[1])}')
print('done...')
