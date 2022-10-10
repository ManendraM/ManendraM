Telugu=int(input("Enter your  Telugu Marks ="))
English=int(input("Enter your English Marks ="))
Maths=int(input("Enter your Maths Marks ="))
Physics=int(input("Enter your Physics Marks ="))
Social=int(input("Enter your Social Marks ="))
c=(Telugu+English+Maths+Physics+Social)/5
if c>90:
    print("🤩🤩🤩,Extraordinary you got {} Percent and Your Grade is A++".format(c))
elif c<90 and c>=80:
    print("Congrats,you got {} Percent and Your Grade is A+.Hope for 90 above".format(c))
elif c<80 and c>=70:
    print("Hmm,you got {} Percent.Hope for 90 above and Your Grade is A".format(c))
elif c<70 and c>=60:
    print("you got {} Percent.Hope for 90 above and Your Grade is B+".format(c))
elif c<60 and c>=50:
    print("Awuful,you got {} Percent.Hope for 90 above and Your Grade is B".format(c))
elif c<50:
    print("😞😞😞,Better Luck Next Time,you got {} Percent.Hope for 90 above".format(c))    

    



