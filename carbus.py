x = int(input())
for i in range(x):
    a, b = map(int, input().split())
    if(a<b):
        print('BIKE')
    elif (a>b):
        print('CAR')
    else:
        print('SAME')