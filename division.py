testCases = int(input())
for i in range(testCases):
    item = int(input())
    if item < 1600:
        print('3')
    
    elif 1600 <= item < 2000:
        print('2')
    
    else:
        print('1')