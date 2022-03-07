testCases = int(input())
for i in range(testCases):
    x1, y1, x2, y2, d = map(int, input().split())
    if x2 * d <= x1 and y2 * d <= y1:
        print("Yes")
    else:
        print("No")
