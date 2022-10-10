#n=int(input("Enter the value of n=")) #7
#for a in range(0,2):
  #  for i in reversed(range (0,2)):
    #    for j in range (1,n+1):
      #       print(a,i,end=' ')
   # print("\r")
#print("\n")


n=int(input("Enter the value of n=")) #8
for i in range(0,2):
    for j in range (0,i):
         for j in range (i,i+1):
             print(j,end=' ')
         print("\r")
print("\n")
