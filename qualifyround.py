x = int(input())
for i in range(x):
    a, b, c = map(int, input().split())
    easy = b * 1;
    hard = c * 2;
    ans = easy + hard
    if(ans >= a):
        print('Qualify')
    else:
        print('NotQualify')