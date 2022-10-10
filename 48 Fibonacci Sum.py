n=int(input("Enter the value of n="))
sum=0
a=0
b=1
for i in range(0,n) :
   c=a+b
   a=b
   b=c
   sum=sum+0+a+b+c
   print(c)
print(sum)
