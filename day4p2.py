import comm
import re

print('start!')

testFilePath = 'day4.txt'

lines = comm.readFileToList(testFilePath)
lines.append('\n')

result = 0
optional = 'cid'
passportStr = ''

def isValidByr(value):
    if len(value) != 4: return False
    value = int(value)
    if value < 1920 or value > 2002:
        return False
    return True

def isValidIyr(value):
    if len(value) != 4: return False
    value = int(value)
    if value < 2010 or value > 2020:
        return False
    return True

def isValidEyr(value):
    if len(value) != 4: return False
    value = int(value)
    if value < 2020 or value > 2030:
        return False
    return True

def isValidHgt(value):
    if value.endswith('cm'):
        value = int(value.replace('cm', ''))
        if value < 150 or value > 193: return False
    elif value.endswith('in'):
        value = int(value.replace('in', ''))
        if value < 59 or value > 76: return False
    else:
        return False
    return True

def isValidHcl(value):
    if not value.startswith('#'): return False
    elif len(value) != 7: return False
    else:
        regexPattern = re.compile('[0-9a-f]+')
        value = value.replace('#', '')
        if regexPattern.fullmatch(value) is None: return False
    return True

def isValidEcl(value):
    l = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value not in l: return False
    return True

def isValidPid(value):
    if len(value) != 9: return False
    return True

def validateFields(fields):
    print(fields)
    for field in fields:
        fieldList = field.split(':')
        name = fieldList[0]
        value = fieldList[1]
        if name == 'byr':
            if not isValidByr(value): return False
        if name == 'iyr':
            if not isValidIyr(value): return False
        if name == 'eyr':
            if not isValidEyr(value): return False
        if name == 'hgt':
            if not isValidHgt(value): return False
        if name == 'hcl':
            if not isValidHcl(value): return False
        if name == 'ecl':
            if not isValidEcl(value): return False
        if name == 'pid':
            if not isValidPid(value): return False

    return True

def validatePassport(ppStr):
    isPP = False
    ppFields = ppStr.strip().split(' ')
    size = len(ppFields)

    if size == 8: 
        if validateFields(ppFields): isPP = True

    if size == 7:
        if optional not in ppStr:
            if validateFields(ppFields): isPP = True

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