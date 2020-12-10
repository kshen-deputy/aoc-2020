import comm

print('start!')

testFilePath = 'day9.txt'

lines = comm.readFileToList(testFilePath)

preambleSize = 25
preambleList = []

def isValid(l, n):
    for i in l:
        if n - i in l: return True
    return False

invalidN = 0

for i, line in enumerate(lines):
    n = int(line)
    if i < preambleSize: 
        preambleList.append(n)
    else:
        if isValid(preambleList, n):
            preambleList.append(n) # add into list
            preambleList = preambleList[1:] # take out first item
        else:
            invalidN = n
            break

print(invalidN) # 1309761972

resultList = []
i = 0
while True:
    n = int(lines[i])
    sumList = sum(resultList)
    if sumList < invalidN:
        resultList.append(n)
        i += 1
    elif sumList == invalidN:
        print(f'this is the result list: {resultList}')
        break
    else:
        resultList = resultList[1:]

resultList.sort()
result = resultList[0] + resultList[-1]
print(f'this is the sorted list: {resultList}')
print(f'this is the result: {result}')
print('done...')
