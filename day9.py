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

for i, line in enumerate(lines):
    n = int(line)
    if i < preambleSize: 
        preambleList.append(n)
    else:
        if isValid(preambleList, n):
            preambleList.append(n) # add into list
            preambleList = preambleList[1:] # take out first item
        else:
            print(f'this is the result: {n}')
            break

print('done...')
