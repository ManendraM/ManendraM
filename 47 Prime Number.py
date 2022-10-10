num = int(input("Enter a number: "))  #5

if num > 1:
   for i in range(2,num):   #2,5  2345
       if (num % i) == 0: 
           print(num,"is not a prime number")
          
   else:
       print(num,"is a prime number")
elif num<0:
    print("enter a valid number")
