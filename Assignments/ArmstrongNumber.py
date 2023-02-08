# 10. Check whether a number is armstrong number.
num = int(input("Enter the number : "))
s = 0
n = num
len1 = len(str(num))
while n > 0:
    digit = n % 10
    s = s + (digit**len1)
    n = n // 10
if s == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")
