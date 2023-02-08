# 1. Multiply all the numbers in a list using function.
# def mult(list1):
#     mul = 1
#     for i in range(len(list1)):
#         mul = mul * list1[i]
#     print("Product of numbers in a list : ", mul)
#
#
# l1 = [2, 4, 6, 1]
# mult(l1)


# 2. Write a Python program to reverse a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"
# def rev(str1):
#     return str1[::-1]
# str1 = "1234abcd"
# rev1 = rev(str1)
# print("Reverse of the string : ",rev1)


# 3. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
# def fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
#
#
# num = int(input("Enter the number : "))
# print(f"Factorial of {num} : {fact(num)}")


# 4. Write a Python function that takes a number as a parameter and check  the number is prime or not.
# def prime(n):
#     flag = 0
#     i = 2
#     while i < n/2:
#         if n % i == 0:
#             flag = 1
#             break
#         i = i + 1
#     if flag == 1:
#         print(f"{n} is not a prime")
#     else:
#         print(f"{n} is prime")
#
#
# n = int(input("Enter the number : "))
# prime(n)

# 5. Create an inner function to calculate the addition in the following way
# •	Create an outer function that will accept two parameters, a and b
# •	Create an inner function inside an outer function that will calculate the addition of a and b
# •	At last, an outer function will add 5 into addition and return it

# def out_fun(a,b):
#     c = 8
#     # inner function - start
#     def in_fun():
#         sum1 = a + b
#         return sum1
#     # inner function - end
#     s1 = in_fun()
#     add1 = s1 + 5
#     return add1
# print("Sum : ",out_fun(4,6))

# 6. Generate a Python list of all the even numbers between 4 to 30.
# Method - 1
# def even(start = 4,end = 30):
#     list1 = []
#     for i in range(start,end):
#         if i % 2 == 0:
#             list1.append(i)
#     print("List : ",list1)
# even()

# Method - 2
# def even():
#     my_list = list(range(4, 30, 2))
#     return my_list
# print("List using range : ", even())
