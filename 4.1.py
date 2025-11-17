height=float(input("Enter your height in inches"))
age=int(input("Enter your age"))


if height >= 48 and age >= 8: 
    print ( "You can ride!")
elif height < 48 and age >= 8:
    print ( "You need to be taller.")
elif height >= 48 and age < 8:
    print ( "You need to be older.")
else:
    print ("You need to be taller and stronger")


    """equal to always after the operator"""