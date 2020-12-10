import comm

print('start!')

testFilePath = 'day6.txt'

lines = comm.readFileToList(testFilePath)
lines.append('\n')

result = 0
formStr = ''

def processForm(formStr):
    nonDupQuestions = []
    for q in list(formStr):
        if q not in nonDupQuestions:
            nonDupQuestions.append(q)
    return len(nonDupQuestions)

for line in lines:
    if line == '\n': # this is the line break -> finish reading a form info
        print(formStr)
        questionNumber = processForm(formStr)
        formStr = ''
        result += questionNumber
    else:
        line = line.replace('\n', ' ')
        formStr += line.strip()


print(result)

print('done...')