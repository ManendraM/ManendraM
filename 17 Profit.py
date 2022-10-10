MNC_price=int(input("Enter the value of MNC PRICE="))
SELLING_price=int(input("Enter the value of SELLING PRICE="))
profit=SELLING_price-MNC_price
if profit>0:
    print("Congrats,you got profit {}".format(profit))
elif profit==0:
    print("you got zero profit {}".format(profit))
elif profit<0:
    print("Sorry,you got lost...hope for next time {}".format(profit))
