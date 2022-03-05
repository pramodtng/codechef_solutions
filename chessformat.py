testCases = int(input())
for i in range(testCases):
    x,y = map(int, input().split())
    tot = x + y
    if tot < 3:
        print("1")
    elif 3 <= tot <= 10:
        print("2")
    
    elif 11 <= tot <= 60:
        print("3")
    
    else:
        print("4")