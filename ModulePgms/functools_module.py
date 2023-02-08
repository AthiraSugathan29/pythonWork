# 1. Sum of the list elements

from functools import reduce
list1 = [1,2,3,4,5]
print(reduce((lambda x,y: x+y),list1))