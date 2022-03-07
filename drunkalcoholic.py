testCases = int(input())
for i in range(testCases):
    steps = int(input())
    if steps%2 == 0:
        print(steps)
    
    else:
        print(steps+2)