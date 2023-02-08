# Arbitary Arguments
def my_func(*names):
    for name in names:
        print("Hi",name,"How are you")

my_func('Athira','Ann')
my_func('Ram')