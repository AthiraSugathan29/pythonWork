# 9. Write a code to find circular rotation of an array by K positions.

arr = [1,2,3,4,5]
d = int(input("Enter the no.of rotations : "))
temp = []
i = 0
n = len(arr)
while (i < d):
    temp.append(arr[i])
    i = i + 1
i = 0
while (d < n):
    arr[i] = arr[d]
    i = i + 1
    d = d + 1
arr[:] = arr[: i] + temp
print("Array after Rotation : ",arr)