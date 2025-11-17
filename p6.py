income = float(input("Enter your annual income: $"))

if income <= 10000:
    tax_owed = 0

elif income <= 40000:
    tax_owed = (income - 10000) * 0.10

elif income <= 85000:
    tax_owed = 3000 + (income - 40000) * 0.22


else:
    tax_owed = 12900 + (income - 85000) * 0.32

print(f"Your taxed income is {tax_owed}")
