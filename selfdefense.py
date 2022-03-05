

x = int(input())
for i in range(x):
    count = 0
    values = int(input())
    items = list(map(int, input().strip().split()))
    for i in items:
        if i in range(10, 60):
            count += 1
    print(count)
    