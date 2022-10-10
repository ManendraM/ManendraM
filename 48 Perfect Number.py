n=int(input("Enter the numbver to check ="))
sum=0
for i in range (1,n):
    if n%i==0:
        sum=sum+i
        if sum==n:
            print("Perferct Number")
        else :
            print("Not a Perfect Number")
