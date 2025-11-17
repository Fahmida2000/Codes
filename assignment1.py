"""Problem 1: Age Category Classifier
Write a program that asks the user for their age and
determines their category:
Input: User's age (integer)
Output: "Minor" (under 18) or "Adult" (18 or older)
Requirements: Handle invalid input (negative numbers)
Enter your age: 16
You are classified as: Minor
"""


input_age = input("Enter your age? ")
age = int(input_age)
if age > 18:
   print ("Adult")

elif age <=0:
   print("invalid input")
   
else:
   print("Minor")