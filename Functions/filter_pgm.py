# 1. Using filter()
# ages = [5, 12, 17, 18, 24, 32]
#
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)
# print(type(adults))
# for x in adults:
#   print(x)

# 2. Using Lambda and filter()
# ages = [5, 12, 17, 18, 24, 32]
#
# adults = filter(lambda x : False if x < 18 else True, ages)
# for x in adults:
#   print(x)

count = 1


def doThis():
    global count
    for i in (1, 2, 3):
        count += 1


doThis()
print(count)