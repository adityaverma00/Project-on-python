print("Welcome to our calculator->")
X = float(input("enter the first number->"))
Y = float(input("enter the second number"))
Z = input("enter sign->")
if Z =='+': #for sum
    sum = X + Y
    print("added", sum)
elif Z == '-': #for substaction
    sub = X - Y
    print("subtracted", sub)
elif Z == '*': #for multiplication
    multiply = X * Y
    print("multiply", multiply)
else:
    Z == '/' #for division
    divide = X / Y
    print("divided", divide)
    



