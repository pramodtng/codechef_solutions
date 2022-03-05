x = int(input())
list = []
for i in range(1,x+1):
    if x%i == 0 and i<10:
        list.append(i)

max_value = max(list)
print(max_value)