n=int(input("Enter the value of n="))

for i in range(1,2):
    for j in range (0,n):
        print()
        
for i in range(1,n+1):
    for j in range (1,j+1):
       print(1,end=" ")
       print(0,end=" ")
    print("\r")  
print("\n")

