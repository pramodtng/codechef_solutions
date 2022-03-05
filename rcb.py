x = int(input())
for i in range(x):
    a, b, c = map(int, input().split())
    totalPoints = (c*2) + a
    if(totalPoints >= b):
        print("Yes")
    else:
        print("No")
