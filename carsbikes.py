values = []
testCases = int(input())
for i in range(testCases):
    items = int(input())
    values.append(items)
for j in values:
    if(j%4 == 2):
        print('Yes')
    else:
        print('No')