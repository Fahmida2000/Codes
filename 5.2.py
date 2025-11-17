number1 = float(input("Input first number"))
number2 = float(input("Input second number"))
operation = input("Select an operation among + - / * ")

if number2==0 and operation=="/":
    print("Cannot divide by zero")
elif operation == "+":
    print (number1 + number2)
elif operation == "-":
    print (number1 - number2)
elif operation == "/":
    print (number1 / number2)
elif operation == "*":
    print (number1 * number2)
else:
    print("Invalid Operation")