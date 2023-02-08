# Factorial of a number
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)


num = int(input("Enter the number : "))
if num < 0:
    print("Invalid number")
elif num == 0:
    print(f"Factorial of {num} is 1")
else:
    print(f"Factorial of {num} : {fact(num)}")