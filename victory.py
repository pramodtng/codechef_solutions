x, y, z = map(int, input().split())
overs = 20 - y
finalAns = overs * 6
a = (finalAns * 6) + z
if(a > x):
    print("Yes")
else:
    print("No")