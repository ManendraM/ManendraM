n=int(input("Enter the value of n="))
sum=0
count=0
while n>0:
    k=n%10
    sum=sum+k
    n=n//10
    count=count+1
print(count)
print(sum)
