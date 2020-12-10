import comm

print('start!')

testFilePath = 'day6.txt'

lines = comm.readFileToList(testFilePath)
lines.append('\n')

result = 0
nonDupQuestions = []

def processForm(nonDupQuestions, formStr):
    print(f'line: {formStr}')
    if not nonDupQuestions: 
        nonDupQuestions = list(formStr)
    else:
        commNonDupQuestions = []
        for q in list(formStr):
            if q in nonDupQuestions:
                commNonDupQuestions.append(q)
        nonDupQuestions = commNonDupQuestions
    return nonDupQuestions

skip = False
for line in lines:
    if line == '\n': # this is the line break -> finish reading a form info
        print('nonDupQuestions: ' + str(nonDupQuestions))
        result += len(nonDupQuestions)
        nonDupQuestions = []
        skip = False
    else:
        line = line.replace('\n', '')
        if not skip: nonDupQuestions = processForm(nonDupQuestions, line)
        if not nonDupQuestions: skip = True


print(result)

print('done...')