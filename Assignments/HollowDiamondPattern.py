# 3. Try to create hollow diamond pattern.
rows = int(input("Enter the rows : "))
for i in range(rows):# 0
    print("   "*(rows-i)+"*",end=" ")
    if i != 0:
        print("   "*(2*i)+"*",end=" ")
    print()
for i in range(rows,-1,-1):
    print("   "*(rows-i)+"*",end=" ")
    if i != 0:
        print("   "*(2*i)+"*",end=" ")
    print()

# rows = 5
# for i in range(rows):
#     print("   "*(rows-i)+"*",end=" ")
#     if i != 0:
#         print("   "*(2*i)+"*",end=" ")
#     print()
# for i in range(rows,-1,-1):
#     print("   "*(rows-i)+"*",end=" ")
#     if i != 0:
#         print("   "*(2*i)+"*",end=" ")
#     print()