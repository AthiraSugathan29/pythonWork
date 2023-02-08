# 6. Write a Python program to sort (ascending and descending) a dictionary by value.
#  Expected O/P:
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original Dictionary : ",dict1)
ascdict = {}
desdict = {}
val_list = list(dict1.values())
revval_list = list(dict1.values())
val_list.sort()
revval_list.sort(reverse=True)
key_list = list(dict1.keys())
for i in val_list:
    index = list(dict1.values()).index(i)
    ascdict[key_list[index]] = i
for i in revval_list:
    index = list(dict1.values()).index(i)
    desdict[key_list[index]] = i
print("Ascending Order : ",list(ascdict.items()),"\nDescending Order : ",desdict)


