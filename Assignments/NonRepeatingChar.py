# 8. Find non-repeating characters in a string.
str1 = input("Enter the string : ")
for i in str1:
    if str1.count(i) == 1:
        print(i,end="")