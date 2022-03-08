from re import A


testCases = int(input())
for i in range(testCases):
    a,b,c = map(int, input().split())
    ans = (b-a)/c
    print(int(ans))