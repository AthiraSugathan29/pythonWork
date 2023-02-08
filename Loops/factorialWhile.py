# Factorial of a number
n = int(input("Enter the number: "))
p = 1
i = 1
while i <= n:
    p = p * i
    i = i + 1
print("Factorial of %d is %d"%(n,p))