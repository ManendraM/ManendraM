n=int(input("Enter the value of n="))
a=0
b=1
for i in range(2,n):
   c=a+b
   a=b
   b=c
   if c<n:
      print(c,end=" ")
   elif c==n:
        print ("break")
   elif c>>n:
       print("invalid")
 
