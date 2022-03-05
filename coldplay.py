from tkinter import Y


testCases = int(input())
for i in range(testCases):
    x,y = map(int, input().split())
    ans = x//y
    print(ans)