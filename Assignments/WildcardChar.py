# 6. Write code to check if two strings match where one string contains wildcard characters.
str1 = input("Enter the 1st string : ")
str2 = input("Enter the 2nd string : ")
special_chr = ['/','*','@','&','!','?']
for i in special_chr:
    str1 = str1.replace(i,"")
    str2 = str2.replace(i,"")
print("S1 : ",str1)
print("S2 : ",str2)
if str1 == str2:
    print("Both strings are same")
else:
    print("Both strings are not same")