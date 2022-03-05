x = int(input())
for i in range(x):
    a,b,c,d = map(int, input().split())
    value1 = a - c
    value2 = b - d
    ans = max(abs(value1), abs(value2))
    print(ans)