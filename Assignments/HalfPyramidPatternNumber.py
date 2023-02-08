# 5. Half pyramid pattern with number.
rows = int(input("Enter the rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print(j+1,end=" ")
    print()