testCases = int(input())
for i in range(testCases):
    x, y,z = map(int, input().split())
    trips = x+y
    if trips < z:
        print('Yes')
    else:
        print('No')