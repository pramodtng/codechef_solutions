x, y = map(int, input().split())
min = x- y
y = y/2
ans = int(min + y)
print(ans)