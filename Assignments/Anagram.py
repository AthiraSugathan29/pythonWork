# 3. Write code to Check if two strings are Anagram or not.

str1 = input("Enter the 1st string : ")
str2 = input("Enter the 2nd string : ")
if sorted(str1) == sorted(str2):
    print("Two strings are Anagram.")
else:
    print("Two strings are not Anagram.")
