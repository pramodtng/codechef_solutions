testCases = int(input())
for i in range(testCases):
    x = int(input())
    ans = x%4
    if ans == 0:
        print("North")
    elif ans == 1:
        print("East")
    elif ans == 2:
        print("South")
    elif ans == 3:
        print('West')