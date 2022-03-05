testCases = int(input())
for i in range(testCases):
    x,y, z = map(int, input().split())
    ans = x+y
    if ans > z:
        print('Train')
    elif ans < z:
        print('Planebus')
    else:
        print('Equal')