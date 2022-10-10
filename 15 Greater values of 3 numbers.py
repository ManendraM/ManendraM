a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
c=int(input("Enter the value of c="))
if a>b>c:
    print("Your value of a {} is greater than b {} greater than c {}".format(a,b,c))
elif b>c>a:
    print("Your value of b {} is greater than c {} greater than a {}".format(b,c,a))
elif c>a>b:
    print("Your value of c {} is greater than a {} greater than b {}".format(c,a,b))
elif c>b>a:
    print("Your value of c {} is greater than b {} greater than a {}".format(c,b,a))
elif b>a>c:
    print("Your value of b {} is greater than a {} greater than c {}".format(b,a,c))
elif a>c>b:
    print("Your value of a {} is greater than c {} greater than b {}".format(a,c,b))    
