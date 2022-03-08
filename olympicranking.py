testCases = int(input())
for i in range(testCases):
    a,b,c,d,e,f = map(int, input().split())
    rankOne = a+b+c
    rankTwo = d+e+f
    if rankOne > rankTwo:
        print('1')
    else:
        print('2')