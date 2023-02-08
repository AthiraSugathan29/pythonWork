# 6. Reverse pattern from 10 to 1.
rows = int(input("Enter the rows: "))
for i in range(0,rows):
    for j in range(rows-i,0,-1):
        print(j,end=" ")
    print()