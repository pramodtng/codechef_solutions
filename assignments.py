testCases = int(input())
for i in range(testCases):
    values = int(input())
    ans = 10 - values
    if ans >= 3:
        print("Yes")
    else:
        print("No")