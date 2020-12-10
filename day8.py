import comm

print('start!')

testFilePath = 'day8.txt'

lines = comm.readFileToList(testFilePath)

# commands: acc, jmp, nop

result = 0
executedCmdIDs = []

curP = 0
curCmd = ''

while True:
    # get current command and argument
    line = lines[curP].replace('\n', '')
    print(line)
    curCmd = line.split(' ')[0]
    arg = line.split(' ')[1]
    # execute command
    if curP not in executedCmdIDs:
        # execute
        if curCmd == 'nop': 
            nextP = curP + 1
        elif curCmd == 'acc':
            result += int(arg)
            nextP = curP + 1
        else:
            nextP = curP + int(arg)
        # add to executed
        executedCmdIDs.append(curP)
        print(f'curP: {curP}, nextP: {nextP}')
        # move to next pointer
        curP = nextP
    else:
        # find the loop!
        print(f'cmd pointer: {curP} has been executed')
        break
    # check next command
    
print(result)
print('done...')
