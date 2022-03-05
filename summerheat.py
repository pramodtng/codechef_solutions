from re import A


testCases = int(input())
for i in range(testCases):
    a,b,c,d = map(int, input().split())
    x = c/a
    y = d/b
    print(int(x+y))