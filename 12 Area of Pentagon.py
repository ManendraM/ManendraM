print("Caluculator to find the Area of an Regular and Irregular Pentagon")
code=(int(input("Enter code equal to 1 if you want to calculate area of a Regular Polygon or Enter code equal to 2 if you want to calculate the area of a irregular polygon:")))
if code==1:
    print("Caluculator to find the Area of an Regular Pentagon")
    p=int(input("Enter The Perimeter of a Pentagon ="))
    q=int(input("Enter The Apothem of a Pentagon ="))
    Area=1/2*p*q
    print("Area of Pentagon for Perimeter {} and Area of a Pentagon for Perimeter {} is {}".format(p,q,Area))
elif code==2:
     print("Caluculator to find the Area of an Irregular Pentagon")
     l=int(input("Enter The Side of a Pentagon ="))
     Area=1.7*l*l
     print("Area of Pentagon for Side {} is {}".format(l,Area))
