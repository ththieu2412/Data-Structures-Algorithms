from math import factorial
#           0C0
#       1C0     1C1
#   2C0     2C1     2C2
#3C0    3C1     3C2     3C3

def Pascal(n):
    for i in range(n):
        for j in range(n-i):
            print(end=" ")

        for j in range(i+1):
            #nCr = n! / ( (n-r)!r! )
            print(factorial(i) // (factorial(j) * factorial(i-j)), end=" ")

        print()

n = int(input("Enter n: "))
Pascal(n)
