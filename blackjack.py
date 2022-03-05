x = int(input())
for i in range(x):
    a, b = map(int, input().split())
    ans = 21 - (a + b)
    if(ans >= 1 and ans <=10):
        print(ans)
    else:
        print('-1')