username= input("Enter the username")
password= input("Enter the password")

if username == "admin" and password == "secure123":
    print ("Welcome Admin")
elif username == "admin" and password != "secure123":
    print("Wrong pass")
else:
    print ("Username not found")