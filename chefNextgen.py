x = int(input())
for i in range(x):
    a, b, x, y = map(int, input().split())
    ans1 = a * b
    ans2 = x * y

    if ans2 >= ans1:
        print('Yes')
    else: 
        print('No') 

