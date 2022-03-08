testCases = int(input())
for i in range(testCases):
    x1,x2,x3,v1,v2 = map(int, input().split())
    x = abs(x1 - x3)/v1
    y = abs(x2 - x3)/v2
    if x < y:
        print('Chef')
    
    elif x > y:
        print('Kefa')
    
    else:
        print('Draw')