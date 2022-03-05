x = int(input())
for i in range(x):
    n,x,p = map(int, input().split())
    wrongAns = n- x
    correctAns = (x * 3) - wrongAns
    if(correctAns >= p):
        print("PASS")
    else:
        print("FAIL")