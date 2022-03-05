testCases = int(input())
for i in range(testCases):
    x, y = map(int, input().split())
    ans = x//2
    if ans <= y:
        print(ans)
    else:
        print(y) 
