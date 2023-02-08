# Strings

str1 = "Hello"
str2 = 4
str3 = str1+" "+str(str2)
print(str3)
print(len(str3))

# While Loop in Strings
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index +1

# For Loop in Strings
fruit = "apple"
for i in fruit:
    print(i)
    print("**")

var1="This	is	a	good example"
str5="is"
print (var1.count(str5)) # count total no: of occurence of 'is' => 2
print (var1.count(str5,4,10)) # count total no: of occurence of 'is' between 4th index and 10th index  => 1