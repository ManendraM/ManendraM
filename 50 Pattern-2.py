n=int(input("Enter the value of n=")) 
for i in reversed(range(0,n+1)): 
    for j in range (1,i+1):
        print("*",end=' ')
    print("\r")
print("\n")
