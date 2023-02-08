# Heart Pattern

rows =9
half = rows // 2
for i in range(2,half):
    print(" "*(half-i-1)+"*"*(2*i+1)+"  "*(half-i)+"*"*(2*i+1))
for i in range(rows,0,-1):
    print(" "*(rows-i)+"*"*(2*i-1))

