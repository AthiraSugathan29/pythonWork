tp1 = (1,"abc",2.3,6,8,"test",99)
print(tp1)
tp2 = (1,(4,5.6,7),"a",True)
print(tp2)
l1 = [1,2,3]
print(tuple(l1))
print(len(tp1))
print(tp1[1])
print(tp2[1:3])
print(tp1[-1])
print(tp1[-2])
print(tp1[::-1])
print(tp1[::-2])
print(tp1[:-1])
print(tp1[:-3])
print(tp1[-4:-1])

# To update a tuple
tp4 = (1,2,3,4,5) # Tuple is immutable.So we couldnot able to change tuple directly.
print(tp4)
l2 = list(tp4) # Convert tuple into a mutable datatype
l2[1] = "Athira" # Then change the value
tp4 = tuple(l2) # Then Convert into tuple
print(tp4)

# To append a value
tp5 = (10,20,30,40,50,60)
print(tp5)
l3 = list(tp5)
l3.append(70)
tp5 = tuple(l3)
print(tp5)

# Add a tuple to an already existing tuple.
tp6 = (4,5,6,7)
tp7 = ("pj","abc")
tp6 += tp7
print(tp6)

# Remove elements from tuple
l4 = list(tp6)
l4.remove("pj")
tp6 = tuple(l4)
print(tp6)

# Delete a tuple
del tp7
# print(tp7)

#For Loop
tp8 = (13,22,35,48,56)
print("For Loop")
for i in range(len(tp8)):
    print(tp8[i])
# Other Method
# for i in tp8:
#     print(i)

# While loop
tp9 = (11,26,23,84,45)
i = 0
print("While Loop")
while i < len(tp9):
    print(tp9[i])
    i += 1


