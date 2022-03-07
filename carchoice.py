testCases = int(input())
for i in range(testCases):
    x1, y1, x2, y2 = map(int, input().split())
    ans = x2/x1
    ans2 = y2/y1
    if ans < ans2:
        print("-1")
    
    elif ans > ans2:
        print('1')
    else:
        print('0')