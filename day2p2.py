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
    p1 = int(ruleList[0].split('-')[0])
    p2 = int(ruleList[0].split('-')[1])
    s = ruleList[1]

    result = string[p1-1: p2]
    # if result.startswith(s) and not result.endswith(s):
    #     print(f'rule: p1: {p1}, p2: {p2}, char: {s}, string: {string}')
    #     return True
    # elif result.endswith(s) and not result.startswith(s):
    #     print(f'rule: p1: {p1}, p2: {p2}, char: {s}, string: {string}')
    #     return True
    # else:
    #     return False

    if (result.startswith(s) and result.endswith(s)) or ( not result.startswith(s) and not result.endswith(s)):
        return False
    else:
        print(f'rule: p1: {p1}, p2: {p2}, char: {s}, string: {string}')
        return True


for line in lines:
    if isValidPassword(line):
        result += 1

print(result)

print('done...')
