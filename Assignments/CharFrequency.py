# 5. Write code to Calculate frequency of characters in a string.
str1 = input("Enter the string : ")
for i in str1:
    freq = str1.count(i)
    print(f"{i} : {freq}")
