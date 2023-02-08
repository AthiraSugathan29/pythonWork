# 1.Write a Python program to access a function inside a function.
def out_fun(a):
    def in_fun(b):
        nonlocal a
        a = a + 1
        return a+b
    return in_fun
func = out_fun(3)
print("Result : ",func(10))

# 2.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
# def square(start,end):
#     list1 = []
#     for i in range(start,end+1):
#         sq = i**2
#         list1.append(sq)
#     return list1
# l1 = square(1,30)
# print("List : ",l1)

# 3.Assign a different name to function and call it through the new name.
# def fun1(a):
#     return a+1
# fun2 = fun1
# print("Result : ",fun2(2))

# 5.Python function that accepts two numbers as arguments and returns the sum.
# def sum1(n1,n2):
#     sum1 = n1 + n2
#     return sum1
#
#
# num1 = int(input("Enter the number : "))
# num2 = int(input("Enter the number : "))
# print(f"Sum : {sum1(num1,num2)}")

# 6.Python function that accepts different values as parameters and returns a list.
# def list1(*lists):
#     l1 = []
#     for i in lists:
#         l1.append(i)
#     return l1
#
# l1 = list1(2,3,5,6)
# print(f"List : {l1}")

# 7.Python function that returns a tuple.
# def tup1(*tup1):
#     l1 = []
#     for i in tup1:
#         l1.append(i)
#     tup = tuple(l1)
#     return tup
#
# t1 = tup1(2,3,5,6)
# print(f"Tuple : {t1}")

# 8.Define a function that accepts 2 values and return its sum, subtraction and multiplication.
# def op(n1,n2):
#     sum1 = n1 + n2
#     sub1 = n1- n2
#     mul1 = n1 * n2
#     return sum1,sub1,mul1
#
#
# num1 = int(input("Enter the number : "))
# num2 = int(input("Enter the number : "))
# sum2, sub2, mul2 = op(num1,num2)
# print(f"Sum : {sum2} \nSubtraction : {sub2} \nMultiplication : {mul2}")

# 9.Define a function that accepts roll number and returns whether the student is present or absent.
# def stud(rn):
#     present1 = [2,3,6,4,8,9,11]
#     if rn in present1:
#         print("Student is Present")
#     else:
#         print("Student is Absent")
# rollno = int(input("Enter the roll number to be checked : "))
# stud(rollno)

# 10.Define a function which counts vowels and consonant in a word.
# def count1(wr):
#     vowels = ['a','e','i','o','u']
#     count_vowels = 0
#     count_con = 0
#     for i in wr:
#         if i in vowels:
#             count_vowels = count_vowels + 1
#         else:
#             count_con = count_con + 1
#     print(f"Count of vowels in {wr} : {count_vowels}")
#     print(f"Count of consonant in {wr} : {count_con}")
# word = input("Enter a word to check : ")
# count1(word)

# 11.Define a function that accepts a number and returns whether the number is even or odd.
# def evenodd(num):
#     if num % 2 == 0:
#         return 1
#     else:
#         return 0
# num = int(input("Enter a number to check : "))
# flag = evenodd(num)
# if flag == 1:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")