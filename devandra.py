testCases = int(input())
for i in range(testCases):
    a,b,c,d,e = map(int, input().split())
    balance = a - b
    expenses = c + d + e
    if(expenses > balance):
        print("No")
    else:
        print("Yes")