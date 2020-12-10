import comm

print('start!')

testFilePath = 'day10.txt'

lines = comm.readFileToList(testFilePath)

lines = list(map(int, lines))
lines.sort()
lines = lines + [lines[-1] + 3]
s = len(lines)
resultDict = {'0': 1}

i = 0
s = len(lines)

while i < s:
    res = 0
    cur = lines[i]
    for k in range(1, 4):
        key = cur - k
        if str(key) in resultDict.keys():
            res += resultDict[str(key)]
    resultDict[str(cur)] = res
    i+=1

print(resultDict)
print('done...')
