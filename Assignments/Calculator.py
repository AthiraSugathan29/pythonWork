# Basic Calculator Program

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter the Operator(+,-,*,/,%,**,//): ")
if c == "+":
    res = a + b
elif c == "-":
    res = a - b
elif c == "*":
    res = a * b
elif c == "/":
    res = a / b
elif c == "%":
    res = a % b
elif c == "**":
    res = a ** b
elif c == "//":
    res = a // b
else:
    res = "Invalid"
print("Result : ",res)
