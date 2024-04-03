import math

#Recursion
def fibonacciRecurion(n):
    if n <= 1:
        return n
    return fibonacciRecurion(n-1) + fibonacciRecurion(n-2)

#Not recursion
def fibonacci(n):
    a = 0
    b = 1
    c = 0
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c

#Other
def fibonaci2(n):
    phi = 1.618
    f = (pow(phi,n) - (1-phi)**n) / math.sqrt(5)
    return round(f)


n = int(input("Nhap vao so nguyen n: "))
if n < 0:
    raise Exception("Nhập n >= 0!")
print(f"So Fibonacci thu {n} (dung de quy) la: {fibonacciRecurion(n)}")
print(f"So Fibonacci thu {n} (khong dung de quy) la: {fibonacci(n)}")

