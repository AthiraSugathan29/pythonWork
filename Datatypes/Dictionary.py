dict1 = {"Name":"Athira","Age":17,"Address":"Muscat","Course":"MCA"}
print(dict1)
print(type(dict1))
print(dict1["Course"])
print(dict1.get("Name"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["Name"] = "Anu"
print(dict1)
dict1.update({"Address":"Kerala","Course":"BCA"})
print(dict1)
dict1["Batch"] = 2019
print(dict1)
dict1.update({"Class":"A","Subject":"Python"})
print(dict1)
dict1.pop("Class")
print(dict1)
dict1.popitem()
print(dict1)
del dict1["Batch"]
print(dict1)
dict2 = {"Brand":"Ford","Model":2017}
# del dict2 # Completely delete dictionary
print(dict2)
dict2.clear()
print(dict2)