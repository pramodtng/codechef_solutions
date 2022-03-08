testCases = int(input())
for i in range(testCases):
    x, y, z = map(int, input().split())
    amtSpent = x * y
    amtRecived = x * z
    profitEarned = amtRecived - amtSpent
    print(profitEarned)