import json

#print(dir(json)) # To get all the directories in json module
x = '{"name":"Anu","Age":19,"Course":"BCA"}' #json
print(x)
print(type(x))

# Parsing Json string to Python dictionary
y = json.loads(x)
print(y)
print(type(y))

#Parsing Python dictionary to Json string
z = json.dumps(y)
print(z)
print(type(z))