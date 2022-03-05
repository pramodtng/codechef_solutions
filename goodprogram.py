x = int(input())
for i in range(x):
    y = int(input())
    ans = y /4
    if(ans%1 == 0):
        print("Good")
    else:
        print("Not Good")