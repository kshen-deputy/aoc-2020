import comm

print('start!')

testFilePath = 'day10.txt'

lines = comm.readFileToList(testFilePath)

lines = list(map(int, lines))
lines.sort()

i = 0
s = len(lines)
oneJoltDiff = 1
threeJoltDiff = 1

while i < s-1:
    curAdapter = lines[i]
    nextAdapter = lines[i+1]
    diff = nextAdapter - curAdapter
    if diff == 1: oneJoltDiff+=1
    elif diff == 3: threeJoltDiff+=1
    else: print(curAdapter)
    i+=1

result = oneJoltDiff * threeJoltDiff
print(result)
print('done...')
