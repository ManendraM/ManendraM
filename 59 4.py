n = int(input("Enter Your Number: ")) 
sum = 0
i = 0
while i <= n:  
    p = i % 100
    if p%4 == 0 :
        sum =sum+p  
        i =i+1  
    else:   
        i+=1 
        continue 

print("Sum is : ",sum)
