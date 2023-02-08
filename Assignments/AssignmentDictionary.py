# 1. Write a Python program to print all unique values in a dictionary.
# list1 = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# set_val = set()
# for i in list1:
#     for val in i.values():
#         set_val.add(val)
# print("Unique Values : ",set_val)

# Another Method
# list2 = []
# for i in list1:
#     list2.extend(list(i.values()))
#     uni_val = set(list2)
# print("Unique Values : ",uni_val)


# 2. Write a Python program to combine values in python list of dictionaries.
#    Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
l1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Method - 1
# l2 = []
# new_dict = {}
# for i in l1:
#     l3 = list(i.values())
#     l2.append(l3[0])
#     l2.append(l3[1])
# print(l2)
# for i in range(0,len(l2),2):
#     if l2[i] in new_dict:
#         rep_key = l2[i]
#         print(rep_key)
#         rep_index = l2.index(rep_key)
#         print(rep_index)
#         l2[rep_index+1] = l2[i+1]+l2[rep_index+1]
#         new_dict[l2[i]] = l2[rep_index+1]
#         print(new_dict[l2[i]])
#     else:
#         new_dict.setdefault(l2[i],l2[i+1])
# print(new_dict)

# Method - 2
list1 = {}
for i in l1:
    if i["item"] not in list1:
        list1[i["item"]] = i["amount"]
    else :
        list1[i["item"]] += i["amount"]
print(list1)
# 3. Write a Python program to create a dictionary from a string.
# str1 = 'Athira'
# str_dict = {}
# Method - 1
# for i in range(1,len(str1)+1):
#     str_dict.setdefault(i,str1[i-1]) #same as get() method, get the value using the key,if the key doesn't exist in the dictionary it will set that key and value to that dictionary as a new item.(Use setdefault() to get the dictionary format also)
# print("Dictionary from the given string : ",str_dict)

#Method - 2
# for i in range(1,len(str1)+1):
#     # str_dict[i] = str1[i-1]
#     str_dict.update({i:str1[i-1]})
# print(str_dict)

# 4. Write a Python program to print a dictionary in table format.
