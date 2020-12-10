import comm

print('start!')

testFilePath = 'day4.txt'

lines = comm.readFileToList(testFilePath)
lines.append('\n')

result = 0
optional = 'cid'
passportStr = ''

def validatePassport(ppStr):
    isPP = False
    size = len(ppStr.strip().split(' '))
    if size == 8: isPP = True
    if size == 7:
        if optional not in ppStr:
            isPP = True
    print(ppStr, f'-----> {isPP}')
    return isPP

for line in lines:
    if line == '\n': # this is the line break -> finish reading a passport info
        isPassport = validatePassport(passportStr)
        if isPassport: result += 1
        passportStr = ''
    else:
        line = line.replace('\n', ' ')
        passportStr += line

print(result)

print('done...')