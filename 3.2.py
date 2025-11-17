age= int(input("Enter your age to get ticket price"))

if age <= 2:
    print("Free")
elif age <= 12:
    print ("$10")
elif age <= 13:
    print ("$20")
else:
    print ("$15")
