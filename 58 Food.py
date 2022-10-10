print("Hello")
print("Welcome to")
print("MV NOVOTEL")
Customer_Name=input("Customer Name : ")
Date=input("Date : ")
Customer_Number=input("Customer Number : ")
Customer_Adress=input("Custmoer Adress : ")
CustomerPurchasedItem =input("Customer Purchased Item: ")
Amount=int(input("Customer no of items : "))
h=int(input("Enter the number of Kilometers="))
if CustomerPurchasedItem=='v' and h==0 and h<3:
    v=120*Amount
    print("Total Amount {}".format(v))
if CustomerPurchasedItem=='v' and h>=3 and h<6:
    v=120*Amount+3*h
    print("Total Amount {}".format(v))
if CustomerPurchasedItem=='v' and h>=6 :
    v=120*Amount+6*h
    print("Total Amount {}".format(v))        
elif CustomerPurchasedItem=='nv' and h==0 and h<3:
    nv=150*Amount
    print("Total Amount {}".format(nv))
elif CustomerPurchasedItem=='nv' and h>=3 and h<6:
    nv=150*Amount+3*h
    print("Total Amount {}".format(nv))
elif CustomerPurchasedItem=='nv' and h>=6:
    nv=150*Amount+6*h
    print("Total Amount {}".format(nv))
print("Thank You")
print("Visit Again")
print("Gives us Rating on www.mvnovotel.com")

