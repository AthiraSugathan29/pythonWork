# 1. Square Pattern using characters.
rows = 5
for i in range(1,rows+1): #rows
    for j in range(1,rows+1):#columns
        if (i == 1 or i == rows or j == 1 or j == rows):
            print(chr(64+i),end=" ")
        else:
            print(" ",end=" ")
    print()