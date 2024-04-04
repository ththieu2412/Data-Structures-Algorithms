def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

def Neper(n):
    e = 0
    for i in range(n):
        a = 1 / factorial(i)
        e += a
    return e

n = int(input("Enter n >= 0: "))
if n <= 0:
    raise Exception("Please enter n >=0")
result = Neper(n)
print(f"Neper of {n}: {result:.2f}")