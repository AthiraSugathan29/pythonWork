# String Indexing and Slicing

str1 = "Hello World"
#Indexing
print(str1[0])
print(str1[3])
#Reverse Indexing
print(str1[-1])
print(str1[-3])

#Slicing

#Positive slicing
print(str1[0:3])
print(str1[2:7])

#Negative slicing
print(str1[:-1]) #remove last character and remaining characters will display in forward
print(str1[:-3]) #remove last 3 characters and remaining characters will display in forward

#Reverse String
print(str1[::-1]) #reverse all characters
print(str1[::-2]) #remove alternative characters and reverse all other characters
print(str1[::-3]) #remove alternative 2 characters and reverse all other characters

print("String Operators")
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.swapcase())
print(str1.title())
print(str1.isupper())
print(str1.islower())
str2 = "hello"
print(str2.isalpha())