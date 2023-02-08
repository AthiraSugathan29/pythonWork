def calculator(func):
    def add(a,b):
        print("Addition : ", (a + b))
    def sub(a,b):
        print("Subtraction : ", (a - b))
    def mult(a,b):
        print("Multiply : ", (a * b))
    def operation(a,b):
        add(a,b)
        sub(a,b)
        mult(a,b)
        return func(a,b)
    return operation
@calculator
def divide(a,b):
    print("Divide : ",(a/b))

divide(8,2)
