# x = lambda a: a + 5
# print(x(5))
#

# x = lambda a,b : a + b
# print(x(2,4))

# def fun1(x):
#     return lambda a : a * x
#
# fun2 = fun1(2)
# print("Result : ",fun2(10))

#1. WAP to create a function that takes 1 argument and that argument will be multiplied by unknown given number.
def fun1(x):
    return lambda a : a * x

fun2 = fun1(3)
print(fun2(6))

#2. WAP to filter a list of integers using lambda.

# list1 = [1,2,3,4,5,6,7,8]
# even = list(filter(lambda a: a % 2 == 0,list1))
# odd = list(filter(lambda a : a % 2 != 0,list1))
# print("Even List : ",even)
# print("Odd List : ",odd)

# 3. If-Else in lambda
# max1 = lambda a,b: a if(a>b) else b
# print(max1(53,8))
