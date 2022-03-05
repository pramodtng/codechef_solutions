

testCases = int(input())
for i in range(testCases):
    a,b,c,d = map(int, input().split())
    if(a+c == 180 or b+d == 180):
        print("Yes")
    else:
        print("No")


