import comm
import math

print('start!')

testFilePath = 'day13.txt'

lines = comm.readFileToList(testFilePath)

departTS = int(lines[0].replace('\n', ''))

def getBuses(allBuses):
    allBuses = allBuses.replace('\n', '')
    allBuses = allBuses.split(',')
    availBuses = []
    for bus in allBuses:
        if bus != 'x': availBuses.append(int(bus))
    return availBuses

buses = getBuses(lines[1])

print(f'{departTS}')
print(f'{buses}')

resultDict = {} # {'busID': 'wait time'}

def processDepartureTime(ts, buses):
    res = {}
    for bus in buses:
        nextD = math.ceil(ts / bus) * bus
        waitTime = nextD - ts
        res[bus] = waitTime
        # print(nextD)
    return res

resultDict = processDepartureTime(departTS, buses)

print(resultDict)

minWaitTime = 999999999
resultBus = 0
for bus in resultDict:
    waitTime = resultDict[bus]
    if waitTime < minWaitTime: 
        minWaitTime = waitTime
        resultBus = bus

result = resultBus * minWaitTime

print(result)
print('done...')
