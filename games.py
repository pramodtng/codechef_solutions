testCases = int(input())
for i in range(testCases):
    x, y = map(int, input().split())
    for j in range(y):
        x += 1
    
    if(x%2 == 0):
        print('Janmesh')
    else:
        print('Jay')