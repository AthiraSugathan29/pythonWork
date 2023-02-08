# String Formatting
name = 'Peter'
age = 25
print('%s is %d years old'%(name,age))
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')

bags = 4
apples_in_bags = 5
print(f'There are total {bags*apples_in_bags} apples')

a = 3
b = 5
print('Sum is {}'.format(a+b))