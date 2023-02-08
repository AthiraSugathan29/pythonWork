# 2. Try to create below designed pattern - Hour glass Pattern
rows = int(input("Enter the rows: "))
for i in range(rows,0,-1):# 5 - No.of rows
    for s in range(rows-i): # 5-5 = 0 - No.of spaces
        print(end=" ")
    for j in range(i):# 5 - No.of stars
        print("*",end=" ")
    print()
for i in range(0,rows): # 0 to 4 - No.of rows
    for s in range(0,rows-i-1): # 4 to 0 - No.of spaces
        print(end=" ")
    for j in range(0,i+1): # 1 - No.of stars
        print("*",end=" ")
    print()