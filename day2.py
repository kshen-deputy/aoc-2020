import comm

print('start!')

testFilePath = 'day2.txt'

lines = comm.readFileToList(testFilePath)
# print(lines)

result = 0

def isValidPassword(line):
    line = line.replace('\n', '')
    rule = line.split(':')[0]
    string = line.split(':')[1].strip()
    ruleList = rule.split(' ')
    l = int(ruleList[0].split('-')[0])
    h = int(ruleList[0].split('-')[1])
    s = ruleList[1]
    print(f'rule: min: {l}, max: {h}, char: {s}, string: {string}')

    currentLen = len(string)
    afterLen = len(string.replace(s, ''))
    diffLen = currentLen - afterLen
    if diffLen >= l and diffLen <= h:
        return True
    else:
        return False

for line in lines:
    if isValidPassword(line):
        result += 1

print(result)

print('done...')