# 1. Reverse a tuple
# tp1 = (10,20,30,40,50)
# print(tp1[::-1])

# 2. To access the value 20 from the tuple
# tp2 = (1,2,40,30,20)
# print(tp2[-1])
# tp3 = (1,2,40,[10,2,39],(30,20,10),40)
# print(tp3[4][1])

# To remove repeated elements from this tuple
# l1 = []
# for i in tp3:
#     if i not in l1:
#         l1.append(i)
# print("After removing repeated elements from the tuple :",tuple(l1))


# 3. Check if all items in the tuple are same.
tp4 = (2,2,2,2,6)
# set1 = set(tp4)
# if len(set1) == 1:
#     print("All items in the tuple are same")
# else:
#     print("All items in the tuple are not same")

# Another Method
flag = 1
for i in tp4:
    for j in range(i,len(tp4)-1):
        if tp4[i] != tp4[j+1]:
            flag = 0
            break
if flag == 1:
    print("All items in the tuple are same")
else:
    print("All items in the tuple are not same")
# 4. Copy specific elements from one tuple to a new tuple
# tp5 = tp3[2:4]
# print("Original Tuple : ",tp3)
# print("Copied Tuple : ",tp5)
#
# # 5. Swap two tuples in python
# t1 = (1,2,3)
# t2 = (4,5,6)
# print("Before swapping")
# print("1st Tuple : ",t1)
# print("2nd Tuple : ",t2)
# temp = t1
# t1 = t2
# t2 = temp
# print("After swapping")
# print("1st Tuple : ",t1)
# print("2nd Tuple : ",t2)