# 1. Try to create Diamond  pattern.
rows = int(input("Enter the rows : "))
for i in range(0,rows): #rows 1
    for k in range(0,rows-i-1):# no.of space 3
        print(" ",end=" ")
    for j in range(0,i+1): #columns 2
        print("  *",end=" ")
    print()
for i in range(rows-1,0,-1):#4 - No.of rows
    for k in range(0,rows-i):#5-4= 1 - No.of spaces
        print(" ",end=" ")
    for j in range(0,i):#4 - No.of stars
        print("  *",end=" ")
    print()