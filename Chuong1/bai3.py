#Recursion
def GCDRecursion(a, b):
    if b == 0:
        return a 
    return GCD(b, a%b)

#Not recursion
def GCD(a, b):
    result = 1
    n = a  if a < b else b
    for i in range(2,n+1):
        if a%i == 0 and b%i == 0:
            result = i
    return result

#Other
def GCDOther(a, b):
    while b:
        a, b = b, a%b
    return a

n = int(input("Enter n: "))
m = int(input("Enter m: "))
if m < 0 or n < 0:
    raise Exception("Enter m, n >= 0, please!")
print(f"GCD({m},{n}) (Not recursion): {GCD(m,n)}")
print(f"GCD({m},{n}) (Recursion): {GCDRecursion(m,n)}")



