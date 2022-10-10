n=int(input("Enter the value of n:"))
esum=0
osum=0
for i in range(1,n+1):
    if i%2==0:
        esum=esum+i
    else :
        osum=osum+i
print("The sum of even numbersn between 1 to {} is {}".format(n,esum))
print("The sum of odd numbersn between 1 to {} is {}".format(n,osum))        
