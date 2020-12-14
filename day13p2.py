import comm
import math

print('start!')

testFilePath = 'day13.txt'

buses = [(i, int(t)) for i, t in enumerate(comm.readFileToList(testFilePath)[1].split(",")) if t != "x"]

multiply = 1
for _, bus in buses:
    multiply *= bus

print(multiply)

res = 0
for i, bus in buses:
    p = multiply // bus
    res += -i * pow(p, -1, bus) * p
print(res % multiply)