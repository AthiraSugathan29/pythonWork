# Sum of natural numbers
n = int(input("Enter the limit: "))
s = 0
i = 1
while i <= n:
    s = s + i
    i = i+1
print("Sum : ",s)