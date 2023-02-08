# Lists
# l1 = ["Welcome","all",4,7]
# print(l1)
#
# # Nested List
# l2 = ["Welcome",[2,4,6],"Hi"]
# print(l2)
#
# #+ve Indexing
# print(l2[0])
# print(l2[0][0])
# print(l2[0][1])
# print(l2[0][1:4])
# print(l2[1])
# print(l2[1][0])
# print(l2[1][1])
# print(l2[2])
# print(l2[2][0])
#
# #-ve Indexing
# print(l2[-1])
# print(l2[-2])
# print(l2[-2][-1])
# print(l2[-2][0])
#
# #Slicing
# print(l2[0:2])
# print(l2[0][:-1])
# print(l2[:-1])
#
# #Reverse the list
# print(l2[::-1])
# print(l2[::-1][0])
# print(l2[::-1][1])
# print(l2[::-2])
# print(l2[::-2][1])
# print(l2[::-3])

#List Appending
l3 = [1,2,3,4]
l3.append(5) # insert an element 5 to list l3
print(l3)

#List insert
l3.insert(1,8) # insert an element 8 in 1st position
print(l3)

#List extend
l4 = ['a','b','c']
l3.extend(l4) # insert several items to a list
print(l3)

#Removing list elements
l5 = [10,20,30,40,50]
l5.remove(20) # To remove given item
print(l5)

#List delete
l6 = [10,20,30,40,50,60]
del(l6[3]) # To delete 3rd position element or delete one or more elements
print(l6)
del(l6) # To delete the list entirely
#print(l6)

#List Clear
l7 = ['p','q','r']
l7.clear() # To clear or empty a list
print(l7)

#List Pop
l8 = [1,3,6,8,9]
l8.pop() # Remove last element from list(by default)
print(l8)
l8.pop(1) # Remove element from given position
print(l8)

#Insert in Nested List
l9 = ['a','b',['c','d'],'e','b','f']
l9[2].insert(1,'x') # insert element 'x' in 1st position of nested list ['c','d'] in 2nd position
print(l9)

#List index
print(l9.index('b')) # Returns index of first matched item

#List Count
print(l9.count('b')) # Returns count of given item
l10 = [1,2,[3,4],5,6,(7,8),9]
print(l10.count([3,4]))
print(l10.count((7,8)))

#List Copy
l11 = [1,2,3]

#Normal copy
l12 = l11
print(l11)
l12.append('b') # Both old list and new list will change while using = method.
print("Old list: ",l11)
print("New List: ",l12)

# Using copy() method
l13 = [4,5,6]
l14 = l13.copy() # Returns a shallow copy of the given list
print(l14)
l14.append('b')
print("Old list: ",l13)
print("New List: ",l14)

# Shallow copy of a list using slicing operator
list1 = [10,20,30]
list2 = list1[:]
list2.append(50)
print("Old list: ",list1)
print("New List: ",list2)

# Reverse List
# Reverse list using slicing operator
t1 = [1,2,[6,7],3,4]
t2 = t1[::-1]
print("Old list : ",t1)
print("New List : ",t2)

# Reverse list using Reverse method
t3 = [8,9,[6,7],13,24]
print("Old list : ",t3)
t3.reverse()
print("Reversed List : ",t3)

# Sort list
#Sort in ascending order
s1 = [58,34,89,12,4,43]
s1.sort()
print("Sort in Ascending Order: ",s1)

#Sort in descending order
s2 = [34,1,87,90,9,74]
s2.sort(reverse=True)
print("Sort in Descending order : ",s2)
