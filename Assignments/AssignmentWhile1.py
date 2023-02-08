# 1. Adding elements to a list using while loop.
# n = int(input("Enter the limit : "))
# My_list = []
# i = 1
# while i <= n:
#     My_list.append(i)
#     i = i + 1
# print("List : ",My_list)

# 2. Finding the average of 5 numbers using while loop.
# i = 1
# s = 0
# while i <= 5:
#     n = int(input("Enter the number %d : "%(i)))
#     s = s + n
#     i = i + 1
# avg = s/5
# print("Sum : ",s)
# print("Average : ",avg)

# 3. Printing the square of numbers using while loop.
# n = int(input("Enter the limit : "))
# i = 1
# while i <= n:
#     sq = i ** 2
#     print(f"Square of {i} : {sq}")
#     i = i + 1

# 4. Reversing a number using while loop in Python
n = int(input("Enter the number to be reversed : "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number : ",rev)

# 5. Finding the sum of even numbers using while loop.
# n = int(input("Enter the limit : "))
# i = 1
# s = 0
# while i <= n:
#     if i % 2 == 0:
#         s = s + i
#     i = i + 1
# print(f"Sum of even numbers from 1 to {n} = {s}")

# 6. Check whether a number is prime or not using while loop.
# n = int(input("Enter a number : "))
# i = 2
# flag = 0
# while i <= n/2:
#     if n % i == 0:
#         flag = 1
#         break
#     i = i + 1
# if flag != 1:
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not prime")

# 7. Print even and odd numbers between 1 to the entered number.
# n = int(input("Enter the limit : "))
# i = 1
# j = 1
# print(f"Even numbers between 1 to {n}")
# while i <= n:
#     if i % 2 == 0:
#         print(i,end=" ")
#     i = i + 1
# print()
# print(f"Odd numbers between 1 to {n}")
# while j <= n:
#     if j % 2 != 0:
#         print(j,end=" ")
#     j = j + 1
