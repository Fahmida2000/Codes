"""Problem 5: Secure Login System
Design a login system with multiple security features:
Features:
3 predefined username/password combinations
Maximum 3 login attempts
Case-insensitive usernames -- ignore
Display remaining attempts after each failure
Output: "Access Granted" or "Account Locked"
Sample Valid Credentials:
admin/password123 • user1/mypass • guest/welcome"""


"""here we wil write codes again and again, without loops 3 times"""
username = input("please enter username")
password = input("password")

username1 = "user1"
password1 = "password1"


username2 = "user2"
password2 = "password2"

username3 = "user3"
password3 = "password3"



if (username == username1 and password == password1) or (username==username2 and password == password2) or (username==username3 and password == password3):
    print("access granted")

else:
    print("2 attempts left")
    username = input("please enter username: ")
    password = input("password: ")

    if (username == username1 and password == password1) or (username == username2 and password == password2) or (username == username3 and password == password3):
        print("login successful") 
    else:
      print("1 attempts left")
      username = input("please enter username: ")
      password = input("password: ")
      
      if (username == username1 and password == password1) or (username == username2 and password == password2) or (username == username3 and password == password3):
               print("login successful")
      else:
               print("account locked")


    
 






