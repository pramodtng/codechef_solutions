testCases = int(input())
for i in range(testCases):
    n, x,y = map(int, input().split())
    ans = (n+1) * y
    if ans > x:
        print("YES")
    
    else:
        print("NO")