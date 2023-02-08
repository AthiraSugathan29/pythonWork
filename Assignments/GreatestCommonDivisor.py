# 2. Write code of Greatest Common Divisor.
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
if n1 > n2:
    temp = n2
else:
    temp = n1
for i in range(1,temp+1):
    if (n1 % i == 0) and (n2 % i == 0):
        gcd = i
print(f"Greatest Common Divisor of {n1} and {n2} is {gcd}")
