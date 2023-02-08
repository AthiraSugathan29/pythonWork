# Sum of natural numbers using Recursion.
def Sum1(num):
    if num == 1:
        return 1
    else:
        return num + Sum1(num-1)

n = int(input("Enter the limit : "))
sum1 = Sum1(n)
print("Sum : ",sum1)