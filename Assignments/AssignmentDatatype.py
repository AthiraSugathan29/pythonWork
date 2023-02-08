# 1. Remove empty strings from a list of strings
# Str1 = [“John”, “ ”,“Jack”,”Emma”,” ”,”Jins”,”Lina”]
# o/p: Str1 = [“John”,“Jack”,”Emma”,”Jins”,”Lina”]

# str1 = ["John"," ","Jack","Emma"," ","Jins","Lina"]
# for i in str1:
#     if i == " ":
#         str1.remove(i)
# print(str1)

# 2. Write a python code to remove all the repeating letters from a each words of a given sentence.
# Eg:  i/p:Let’s google the pineapple
#  	   o/p:Let’s gole the pineal

str2 = "Let’s google the pineapple"
str3 = str2.split(" ")
str4 = ''
str5 = ''
for i in str3:
    str4 = dict.fromkeys(i)
    str6 = "".join(str4)
    str5 = str5 + str6 + " "
print(str5)

# Another Method
# str4 = " "
# for i in str3:
#     l = ""
#     for j in i:
#         if j in l:
#             continue
#         else:
#             l = l + j
#     str4 = " ".join(str4)
# # str4 = str4.append(l)
# print(str4)
# 3. Replace each special symbol with # in the following string
#   str1 = '/*Jon is @developer & musician!!'
#  o/p:    ##Jon is #developer # musician##

# str1 = '/*Jon is @developer & musician!!'
# special_chars = ['*','!','/','&','@']
# for i in special_chars:
#     if i in str1:
#         str1 = str1.replace(i,"#")
# print(str1)

# 4. Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print("Reversed List : ",list1)

# 5. Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print("List : ",list1)