testCases = int(input())
for i in range(testCases):
    x, y = map(int, input().split())
    if(x > 0 and y > 0):
        print("Solution")
    
    elif x == 0:
        print("Liquid")
    
    else:
        print("Solid")