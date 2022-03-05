testCases = int(input())
for i in range(testCases):
    items = list(map(int, input().split()))
    for i in range(len(items)):
        bad, good = 0, 0
        if items[i] == 1:
            good = good + 1
        else:
            bad  = bad  + 1
    if good > bad:
        print('Yes')
    else:
        print('No')