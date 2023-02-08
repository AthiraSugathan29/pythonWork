#Identity Operators
# is, is not

a =["apple","mango"]
b =["apple","mango"]
c = a
print(a is c) # Returns true, a and c are same object
print(a is b) # Returns false, a and b are not same object

print(a is not c) # Returns False, a and c are same object
print(a is not b) # Returns True, a and b are not same object
