units= int(input("Enter the no.of units consumed:"))
if units>0 and units<=100:
        amount=units*3.0
elif units>100 and units<=200 :
        amount=units*4.0
elif units>200 and units<=300 :
        amount=units*5.5
elif units>300 and units<=350 :
        amount=units*6.5
elif units>350 and units<=400 :
        amount=units*7.0
else:
        amount=units*7.5

print("Your Electricity Amount is:{}".format(amount))

