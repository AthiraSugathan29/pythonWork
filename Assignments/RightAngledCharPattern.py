# 7. Right-Angled Pattern With Characters.
# rows = int(input("Enter the rows: "))
# count = 0
# for i in range(rows):
#     for j in range(i+1):
#         print(chr(65 + count),end=" ")
#         count += 1
#     print()

# 8. Equilateral Triangle Pattern With Characters.
# rows = int(input("Enter the rows: "))
# count = 0
# for i in range(rows):
#     for s in range(rows-i-1):
#         print(end=" ")
#     for j in range(i+1):
#         print(chr(65 + count),end=" ")
#         count+=1
#     print()

# 9. To print the character of first letter of your name.
# rows = 6
# for i in range(rows):
#     print(" "*(rows-i)+"*",end=" ")
#     if i != 0:
#         if i == 3:
#             print(" "+" *  "*2,end=" ")
#         else:
#             print(" "*(2*i)+"*",end=" ")
#     print()

# 10. Cross number pattern
rows = 6
for i in range(rows,-1,-1):
    print(" "*(rows-i),i+1,end=" ")
    if i != 0:
        print(" "*(2*i),i+1,end=" ")
    print()
for i in range(1,rows+1):
    print(" "*(rows-i),i,end=" ")
    print(" "*(2*i),i,end=" ")
    print()

