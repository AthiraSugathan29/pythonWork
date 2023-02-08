# 1. Write a program to get a string from a given string where all the occurances of it's first char have been
# changed to '$', except the first char itself.
# i/p : "restart"
# o/p : "resta$t"

# str1 = 'restart'
# str2 = str1.lower()
# for i in range(1,len(str1)):
#     if str2[0] == str2[i]:
#         str1 = str1[:i] + '$' + str1[i+1:]
# print(str1)

# 2. Write a python pgm that takes a list of words and returns the length of longest one.
l1 = ['hi','hello','python','test']
print("List1 : ",l1)
temp = ''
templen = 0
firstlen = len(l1[0])
for i in range(len(l1)):
    if len(l1[i]) > firstlen:
        firstlen = len(l1[i])
        temp = l1[i]
        templen = len(l1[i])
print("Longest word : ",temp)
print("Length of the longest word : ",templen)