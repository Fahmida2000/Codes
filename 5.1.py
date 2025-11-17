order= float(input("Enter total order value"))

"""if order >= 50: 
    print ("Free")"""

if order <= 49.99 and order > 30 :
    print ("$", 5 + order)
elif order < 30 :
     print ("$", 10 + order)
else:
    print ("free shipping")