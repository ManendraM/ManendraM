num=int(input("Enter the value of n="))
m=num
while n>0:
     k=num%10
     rev=rev*10+k
     n=num//10
if n==m:
    print("it is a palindraome")
