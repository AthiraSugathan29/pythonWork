# 4. Create inverted full pyramid pattern.
rows = int(input("Enter the rows: "))
for i in range(rows,0,-1):
    for s in range(rows-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print("\n")
