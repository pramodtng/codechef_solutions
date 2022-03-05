testCases = int(input())
for i in range(testCases):
    x, y, z = map(int, input().split())
    ans = y * z
    if ans >= x:
        print('No')
    else:
        print('Yes')