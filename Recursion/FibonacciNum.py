# Fibonacci Series
def fibo(n):
    a = 0
    b = 1
    f = 0
    while a <= n:
        f = a + b
        print(a)
        a = b
        b = f



n = int(input("Enter the limit : "))
for i in range(1,n):
    print(fibo(n))