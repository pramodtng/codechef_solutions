x, y = map(str, input().upper().split())

#R, G & B
#Brown is the most common out of three.

if(x=="R" and y=="B"):
    print("R")
elif(x=="B" and y=="B"):
    print("B")
elif(x=="R" and y=="R"):
    print("R")
elif(x=="G" and y=="G"):
    print("G")
elif(x=="B" and y=="G"):
    print("B")
elif(x=="B" and y=="R"):
    print("R")
elif(x=="R" and y=="G"):
    print("R")
elif(x=="G" and y=="R"):
    print("R")
elif(x=="G" and y=="B"):
    print("B")

