# 11. Write a program to check whether a character is a vowel or consonant
ch = input("Enter the character : ")
vowel = ['A','E','I','O','U','a','e','i','o','u']
if ch in vowel:
    print(f"{ch} is a vowel")
else:
    print(f"{ch} is a consonant")
