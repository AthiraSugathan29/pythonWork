# 4. Write code Check if the given string is Palindrome or not.
str1 = input("Enter the string : ")
str2 = str1.lower()
str3 = str2[::-1]
if str2 == str3:
    print("Given String is Palindrome.")
else:
    print("Given String is not Palindrome.")
