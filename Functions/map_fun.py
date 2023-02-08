# 1. Find length of each items
# def test(x):
#     return len(x)
# a = map(test,("apple","orange","banana","watermelon"))
# print(list(a)) #convert the map into a list, for readability

# 2. Concatenate two list elements using map()
# def fun1(x,y):
#     return x+y
#
# a = map(fun1,["apple","grapes"],["orange","watermelon"])
# print(list(a))

# 3. Concatenate two list elements using map() and lambda

fun2 = map(lambda x,y: x + y,['apple','grapes'],['orange','watermelon'])
print(list(fun2))