# Assignment Loop

# 1. Half pyramid pattern with number.
# r = int(input("Enter the rows : "))
# for i in range(1,r+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

# 2. Reverse pattern from 10 to 1.
# r = int(input("Enter the rows : "))
# for i in range(0,r):
#     for j in range(r-i,0,-1):
#         print(j,end=" ")
#     print()

# 3. Full Pyramid with star.
rows = int(input("Enter the rows : "))
for i in range(rows): #rows
    for k in range(rows-i-1): # no.of space
        print(end=" ")
    for j in range(i+1): #columns
        print("*",end=" ")
    print()
