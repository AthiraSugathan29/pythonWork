# Not a decorator function. It's just a first class function.
# def outer(fun):
#     def inner():
#         result = fun()
#         return result.upper()
#     return inner
#
# def getText():
#     return "hello"
#
#
# func = outer(getText)
# print(func())

# Using decorator
def outer(fun):
    def inner(name):
        result = fun(name)
        return result.upper()
    return inner

@outer
def new_fun(n):
    return "hello " + n

print(new_fun("Athira"))