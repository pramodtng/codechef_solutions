testCases = int(input())
for i in range(testCases):
    x, y = map(int, input().split())
    ans = x * 10 + y * 5
    print(ans)