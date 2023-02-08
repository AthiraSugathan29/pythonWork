# all() method
print("all() method")
t1 = (1,2,0,False) # Returns false if all elements in tuple are not True (ie, tuple contains 0 or false)
print(all(t1))

t2 = (1,2,3)
print(all(t2)) # Returns True if all elements in tuple are True(ie, tuple doesnot contain 0 or False)

t3 = ()
print(all(t3)) # Returns True if the tuple is empty.

# any() method
print("\nany() method")
t1 = (1,2,0,False)
print(any(t1)) # Returns True if any elements of the tuple is True.(ie, other than 0 and False)

t2 = (1,2,3)
print(any(t2))

t3 = ()
print(any(t3)) # Returns False if the tuple is empty.

t4 = (0,False)
print(any(t4)) # Returns False because no element in the tuple is True

#len() method
t5 = (23,"test",8.9,[2,3,5],(74,89))
print("\nlen() method")
print("Length of tuple : ",len(t5))

#max() method
t6 = (64,89,90,90.4,11.8)
print("\nmax() method")
print("Max1 : ",max(t6))

t7 = ("black","white","blue","red")
print("Max2 : ",max(t7))

t8 = ([61,2.3,2],[65,8],[56,23])
print("Max3 : ",max(t8))

#min() method
print("\nmin() method")
print("Min1 : ",min(t6))

print("Min2 : ",min(t7))

print("Min3 : ",min(t8))

#sorted() method
print("\nsorted() method")
print("Sorted list : ",sorted(t6))
print(t6)

#sum() method
print("\nsum() method")
print("Sum : ",sum(t6))

#tuple() method
print("\ntuple() method")
l1 = [2,4,6]
print(tuple(l1))

# enumerate() method
print("\nenumerate() method")
tp1 = ('red','green','blue','orange')
x = enumerate(tp1)
print("Enumerate1 : ",tuple(x))

names = ['Anu','Ram','Sam']
ages = [30,19,25]
print("Enumerate2")
for i,(name,age) in enumerate(zip(names,ages)):
    print(i," ",name," ",age)

print("Enumerate3")
letters = [('a','A'),('b','B')]
for i,letter in enumerate(letters):
    print("Letter %d is %s/%s"% (i,letter[0],letter[1]))

print("map()")
l1 = ['sat','bat','cat']
x = list(map(tuple,l1))
print(x)