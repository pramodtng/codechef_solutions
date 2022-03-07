testCases = int(input())
for i in range(testCases):
    x, y = map(int, input().split())
    count = 0
    for i in range(x, y+1):
        if(i%10 == 2 or i%10 == 3 or i%10 == 9):
            print(i)
            count += 1
    print(count)