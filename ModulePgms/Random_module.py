import random
print(dir(random))
print(random.random())
print(random.randint(1,100))
print(random.randrange(1,10,2))
num = [2,5,1,8,3]
print(random.choice(num))
random.shuffle(num)
print(num)

