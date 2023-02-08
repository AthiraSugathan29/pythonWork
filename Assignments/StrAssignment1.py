# 1. Check if each word in a string begins with a capital letter
str1 = "Hello World"
print(str1.istitle())

# 2. Check if a string contains a specific substring
str2 = "Welcome to Python"
print("Python" in str2)

# 3. Find the index of the first occurrence of a substring in a string
str3 = "Welcome to Programming"
print(str3.find("o"))

# 4. Count the total number of characters in a string
fruit = "Pineapple"
print(len(fruit))

# 5. Count the number of a specific character in a string
msg = "Good Morning"
print(msg.count("o"))

# 6. Capitalize the first character of a string
str4 = "python"
print(str4.capitalize())

# 7. Check if a string contains only numbers
str5 = "Hello123"
print(str5.isnumeric())

# 8. Split a string on a specific character
str6 = "Programming"
print(str6.split("a"))

# 9. Reverse the string "hello world"
str7 = "hello world"
print(str7[::-1])

# 10. Join a list of strings into a single string,delimited by hyphens
t1 = "red"
t2 = "blue"
t3 = "green"
t4 = "-".join([t1,t2,t3])
print(t4)

s1 = ["apple","grapes","orange"]
s2 = "-".join(s1)
print(s2)

# 11. Example of string slicing
txt = "Python Programming"
print(txt[7:14])

# 12. Convert an integer to a string
a = 123
b = str(a)
print(b)
print(type(b))

# 13. Replace all instances of a substring in a string
c = "Welcome Ram"
print(c.replace("Ram","John"))

# 14. Remove whitespace from left,right or both sides of a string
txt1 = " Apple "
print(txt1.lstrip())
print(txt1.rstrip())
print(txt1.strip())

# 15. Strings to be immutable in Python
text = "Hello"
print(text[1])
#text[1] = "X"
print(text[1])
