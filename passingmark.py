testCases = int(input())
for i in range(testCases):
    a,b,c,d,e,f,g = map(int, input().split())
    totalMarks = e+f+g
    if e >= a and f >= b and g >= c and totalMarks >= d:
        print("Yes")
    else:
        print("No")
        