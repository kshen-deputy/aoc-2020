import comm

print('start!')

testFilePath = 'day7.txt'

lines = comm.readFileToList(testFilePath)

resultList = []

# bagsStr - 5 clear lime bags, 3 muted gold bags.
# bagsStr - no other bags.
def processValues(bagsStr):
    bagsStr = bagsStr.replace('.', '')  # take out ending '.'
    bagsList = bagsStr.split(',')
    values = []
    for bagStr in bagsList:
        bagStr = bagStr.strip() # take out starting and ending space
        # print(bagStr)
        if 'no other' in bagStr: values.append('no other')
        else:
            bagStrList = bagStr.split(' ')
            values.append(bagStrList[1] + ' ' + bagStrList[2])
    return values

def processDict(lines):
    d = {}
    for line in lines:
        line = line.replace('\n', '')
        # print(line)
        ruleList = line.split('contain')
        key = ruleList[0].replace('bags', '').strip()
        values = processValues(ruleList[1])
        d[key] = values
        # print(f'"{key}"->"{values}"')
    return d
    
ruleDict = processDict(lines)

# rule dict structure - a dict of lists
# {'vibrant teal': ['pale white', 'clear gold', 'striped white'], ...}
# print(ruleDict)

def processBag(keyword, processList):
    for key in ruleDict:
        value = ruleDict[key]
        if keyword in value and key not in processList:
            print(f'{key}->{value}')
            processList.append(key)
            processBag(key, processList)
    

processBag('shiny gold', resultList)

result = len(resultList)
print(result)

print('done...')