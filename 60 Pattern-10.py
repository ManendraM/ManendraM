n=int(input("Enter the value of n="))
for i in range(0,n+1):
    for k in range(n-i):
        print(' ',end=" ")
    for j in range (1,i+1): 
        print("*",end=' ')
    print("\n")
