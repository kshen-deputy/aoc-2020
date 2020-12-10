import comm

print('start!')

testFilePath = 'day1.txt'
target = 2020

lines = comm.readFileToList(testFilePath)
lines = list(map(int, lines))

def get2sumResult(list, target):
    result = []
    for n in list:
        res = target - n
        if res in list and res not in result:
            result.append(res)
            result.append(n)
            return result
    return result

resultList = []
for n in lines:
    res = target - n
    lines.remove(n)
    resultList = get2sumResult(lines, res)
    if resultList != []:
        resultList.append(n)
        print(resultList)
        break

result = 1
for n in resultList:
    result *= n

print(result)

print('done...')