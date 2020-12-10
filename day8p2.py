import comm

print('start!')

testFilePath = 'day8.txt'

lines = comm.readFileToList(testFilePath)

# commands: acc, jmp, nop

curP = 0
curCmd = ''

def isValidProgram(lines):
    cP = 0
    executedCmdIDs = []
    s = len(lines)
    result = 0
    while True:
        if cP == s: # this is the end
            print(f'reach the end, result -> {result}')
            return True
        line = lines[cP].replace('\n', '')
        curCmd = line.split(' ')[0]
        arg = line.split(' ')[1]
        if cP not in executedCmdIDs:
            # execute
            if curCmd == 'nop': 
                nextP = cP + 1
            elif curCmd == 'acc':
                result += int(arg)
                nextP = cP + 1
            else:
                nextP = cP + int(arg)
            executedCmdIDs.append(cP)
            cP = nextP
        else:
            return False
    return True

while True:
    # get current command and argument
    line = lines[curP].replace('\n', '')
    print(line)
    curCmd = line.split(' ')[0]
    arg = line.split(' ')[1]
    # execute command
    if curCmd == 'nop':
        altCmd = 'jmp'
        lines[curP] = altCmd + ' ' + arg
        if isValidProgram(lines): 
            print(f'got valid program here in line {curP}!!!')
            break
        else:
            lines[curP] = curCmd + ' ' + arg
            curP = curP + 1
    elif curCmd == 'jmp':
        altCmd = 'nop'
        lines[curP] = altCmd + ' ' + arg
        if isValidProgram(lines): 
            print(f'got valid program here in line {curP}!!!')
            break
        else:
            lines[curP] = curCmd + ' ' + arg
            curP = curP + int(arg)
    else:
        curP = curP + 1

    
# print(result)
print('done...')
