# Find elements from list contains 'p' letter
# fruits = ['apple','banana','grapes','cherry']
# newlist = [x for x in fruits if 'p' in x]
# print(newlist)

#
list1 = 'human'

#Number List divisible by 2 and 5 b/w 1 to 100
# num_list = [x  for x in range(1,100) if x % 2 == 0 if x % 5 == 0]
# print("Num List divisible by 2 and 5 : ",num_list)

# Prime Number b/w 1 to 20
# prime = [x for x in range(2,21) if all(x % y !=0 for y in range(2,x))]
# print(prime)

# Find even and odd list
# even = [x for x in range(1,10) if x % 2 == 0]
# odd = [x for x in range(1,10) if x % 2 != 0]
# print("Even list : ",even)
# print("Odd List : ",odd)

# Sum of natural numbers upto 10 using sum()
# num = sum(x for x in range(1,int(input("Enter the limit : "))+1))
# print(num)

# Sum of natural numbers using equation n*(n+1))/2
num = [(x*(x+1))/2 for x in range(1,int(input("Enter the limit : "))+1)]
print(num)