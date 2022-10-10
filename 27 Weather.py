print("Weather in your Area")
Date=(input("Date="))
Temperature=int(input("Enter the Temperature in Degree Celcius="))
if Temperature<0:
    print("Then the weater in Your Area is Freezing Weather")
elif Temperature>0 and Temperature<=10:
    print("Then the weather in Your Area is Very Cold Weather")
elif Temperature>10 and Temperature<=20:
    print("Then the Weather in Your Area is Normal in Temperature")
elif Temperature>20 and Temperature<=30:
    print("Then the Weather in Your Area is Hot in Temperature")
else:
    print("Then the Weather in your Area is TOO Hot in Temperature")
    
