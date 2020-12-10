import comm

print('start!')

testFilePath = 'day7.txt'

lines = comm.readFileToList(testFilePath)

def howManyBags(bagName, bagCount, resultList):
    for line in lines:
        if bagName + ' bags contain' in line:
            line = line.replace('\n', '')
            ruleList = line.split('contain')
            containedBagsStr = ruleList[1]

            if 'no other' in containedBagsStr:
                return '' # this is the bottom, no need to do anything
            else:
                containedBagsStr = containedBagsStr.replace('.', '')
                containedBags = containedBagsStr.split(',')
                # print(containedBags)
                res = 0
                for bagStr in containedBags:
                    bagStr = bagStr.strip()
                    bagStrList = bagStr.split(' ')
                    count = int(bagStrList[0])
                    name = bagStrList[1] + ' ' + bagStrList[2]
                    res = count * bagCount # get how many bags needed in current level
                    resultList.append(res)
                    howManyBags(name, count * bagCount, resultList) # keep going
                return res

resultList = []

# start from top
howManyBags('shiny gold', 1, resultList)

print(sum(resultList))

print('done...')