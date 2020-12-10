import comm

print('start!')

testFilePath = 'day1.txt'
target = 2020

lines = comm.readFileToList(testFilePath)
lines = list(map(int, lines))

results = []

for line in lines:
    res = target - line
    if res in lines and res not in results:
        results.append(res)
        results.append(line)
        print(line * res)



print('done...')