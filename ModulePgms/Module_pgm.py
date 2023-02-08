# Write a pgm to generate
# a random color hex,
# random alphabetical string,
# random value between two integers ,
# random multiple of 7 between 0 and 70
# Hint :  Use random.randint
import random

# a random color hex
rand = random.randint(0,16773456)
hex_num = str(hex(rand))
print(hex_num)
hex_num = hex_num[2:]
if len(hex_num) < 6:
    hex_num = "0"+hex_num
hex_num = '#'+hex_num
print(hex_num)

# Random alphabetical string
str1 = ['hi','hello','test','Python','C','C++']
print(random.choice(str1))

# Random value between two integers
print(random.randrange(20,40))

# Random multiple of 7 between 0 and 70
print(random.randint(0,10)*7)