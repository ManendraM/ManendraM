print("If code equal to [Even] then you will get the sum of even or if code equal to [Odd] then you will get the value of sum of odd")
n=int(input("Enter the value of upto which you need SUM="))
l=int(input("Enter the CODE="))
esum=0
osum=0
if n==1:
    for i in range(1,n+1):
        if i%2==0:
            esum=esum+i
            print("The sum of the EVEN Integers from 0 to {} is {}".format(i,esum))
elif n==2:
     for i in range(1,I+1):
         if i%2!=0:
             osum=osum+i
             print("The sum of the ODD Integers from 0 to {} is {}".format(i,osum))
           

    
