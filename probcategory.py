testCases = int(input())
for i in range(testCases):
    values = int(input())
    if(1 <= values < 100):
        print("Easy")
    
    elif 100 <= values < 200:
        print("Medium")
    
    else:
        print('Hard')