# 1. Write a python program to convert  a   string to tuple.
str1 = "Athira"
tp1 = tuple(str1)
print(tp1)

# 2.Write a python program to convert a list to a tuple.
l1 = [2,3,"hi",9]
print(tuple(l1))

# 3.Write a python program to find repeated items from a tuple.
tp2 = (1,2,4,2,5,8,4)
print(tp2)
set1 = set()
for i in tp2:
    if tp2.count(i) > 1:
        set1.add(i)
print("Repeated items are ",tuple(set1))