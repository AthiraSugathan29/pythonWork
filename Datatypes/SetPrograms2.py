# 1. Add a list of elements to a set.
set1 = {1,2,3,4}
list1 = [10,20,30,40]
print("Set1 : ",set1)
print("List1 : ",list1)
set1.update(list1)
print("After adding list to a set : ",set1)

# 2. Get only unique items from two sets.
s1 = {1,2,3,4}
s2 = {3,2,7,8}
print("Set1 : ",s1)
print("Set2 : ",s2)
s3 = s1.union(s2)
print("Unique items from two sets  : ",s3)

# 3. Check if two sets have any elements in common.If yes, display common elements.
s1 = {"a","b","c"}
s2 = {"p","q","b","a","r"}
if s1.isdisjoint(s2):
    print("Two sets have no common elements")
else:
    print("Two sets have common elements")
    print("Common elements : ",s1.intersection(s2))

# 4. Remove items from set1 that are not common to both set1 and set2.
s1 = {5,6,3,7}
s2 = {6,9,3,8,2}
s1.intersection_update(s2)
print(s1)