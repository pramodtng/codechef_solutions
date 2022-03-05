testCases = int(input())
for i in range(testCases):
    x, y, z = map(int, input().split())
    ans = min(x*y, x+z)
    print(ans)