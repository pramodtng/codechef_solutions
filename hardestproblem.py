testCases = int(input())
for i in range(testCases):
    x, y, z = map(int, input().split())
    if(x < y and x < z):
        print("Draw")
    elif (y < x and y < z):
        print("Bob")
    else:
        print('Alice')