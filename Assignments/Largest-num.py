# Program to find largest among 3 numbers

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
if a >= b:
    if a >= c:
        print("a is greater")
    else:
        print("c is greater")
elif b >= a:
    if b >= c:
        print("b is greater")
    else:
        print("c is greater")
