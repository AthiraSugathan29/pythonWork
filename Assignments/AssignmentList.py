# Assignment List
# 1. Sum all the items in a list

# Method - 1
My_list = [1,2,3,4,5]
sum1 = 0
for i in range(0,len(My_list)):
    sum1 = sum1 + My_list[i]
#print("Sum : ",sum1)

# Method - 2
sum2 = sum(My_list)
#print("Sum using sum() : ",sum2)

# 2. Write a Python program to get the largest number from a list.

# Method - 1
List1 = [1,2,-8,0]
num1 = List1[0]
for i in range(0,len(List1)):
    if num1 < List1[i]:
        num1 = List1[i]
print("Largest Number : ",num1)

# Method - 2
num2 = max(List1)
#print("Largest Number using max() : ",num2)

# 3. Write a Python program to convert a list of characters into a string.
s = ['p','y','t','h','o','n']
str1 = ''.join(s)
#print(str1)

# 4. Write a Python program to multiply all the items in a list.
l1 = [5,4,1,6]
mul = 1
for i in range(0,len(l1)):
    mul = mul * l1[i]
#print("Result : ",mul)
