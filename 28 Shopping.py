Coustmer_Name=input("Coustmer Name:")
Date=input("Date:")
Coustmer_Number=input("Coustmer Number:")
Coustmer_Adress=input("Coustmer Adress:")
amount=int(input("Enter the amount :"))
if amount>0 and amount<=1000:
    Payable_Amount=amount
    print("Total Amount:{}".format( Payable_Amount))
elif amount>1000 and amount<=5000:
    x=amount/10
    Payable_Amount=amount-x
    print("Total Amount:{}".format( Payable_Amount))
elif amount>5000 and amount<=10000:
    x=amount/20
    Payable_Amount=amount-x
    print("Total Amount:{}".format( Payable_Amount))
else :
    x=amount/50
    Payable_Amount=amount-x
    print("Total Amount:{}".format( Payable_Amount))
print("Thank You")
print("Visit Again")
print("The items can be exchanged with in 10 days of buying")
