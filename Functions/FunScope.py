# Local Scope
# def local_scope():
#     msg = "Hello World"
#     print(msg)
#
#
# local_scope()

# Global Scope
# def global_scope():
#     print("Inside Function : ",msg)
#
#
# msg = "Hello World"
# global_scope()
# print("Outside Function : ",msg)

# Global Variable
# def local_scope():
#     global msg
#     msg = "Hello World"
#
#
# local_scope()
# print(msg)

# Non-local Variable
def out_fun():
    x = "Anu"
    def in_fun1():
        x = "Sam"
    def in_fun2():
        nonlocal x
        x = "Jiya"
    def in_fun3():
        x = "Heera"
    in_fun2() # Calling nested function in_fun2() inside out_fun()
    print("Name : ",x)
out_fun()