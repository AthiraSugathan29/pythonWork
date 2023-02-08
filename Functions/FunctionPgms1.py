# 1.Write a python function to find the Max of 3 numbers
def max1(*a):
    print(max(a))
    # Another Method
    # print(f"Max of given 3 numbers {a},{b},{c} is {max(a,b,c)}")
max1(45,92,55)

# 2.Write a python function to sum all the numbers in a list
def sum1(list1):
    # print("Sum of all the numbers in list : ",sum(list1))
    # Another Method
    sum1 = 0
    for i in list1:
        sum1 = sum1 + i
    print("Sum of all the numbers in list : ",sum1)

sum1([5,2,6,4,1])

# 3. Write a python function to multiply all the numbers in a list
def mult(list1):
    mul = 1
    for i in list1:
        mul = mul * i
    print("Product of all numbers in a list : ",mul)

# mult([2,5,1,3])