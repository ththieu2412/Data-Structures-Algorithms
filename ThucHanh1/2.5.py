#Walrus

# walrus operator creates an assignment expression
print("walrus operator creates an assignment expression")
is_new = True
print(is_new)
print("--------------------------------------------\n")

print(is_new := True)

words = ['falcon', 'sky', 'ab', 'water', 'a', 'forest']

for word in words:
    if ((n := len(word)) < 3):
        print(f'warning, the word {word} has {n} characters')
print("--------------------------------------------\n")

#Type hints
def say_hi(name):
    return f'Hi {name}'

greeting = say_hi('John')
print(greeting)

print("--------------------------------------------\n")
def say_hi(name: str) -> str:
    print(type(name))
    return f'Hi {name}'

greeting = say_hi('John')
print(greeting)

greeting = say_hi(123)
print(greeting)
print("--------------------------------------------\n")

#Lamda
# lambda arguments : expression
print("lambda arguments : expression")

#x(5): 5 + 10
x = lambda a : a + 10
print(x(5))
print("--------------------------------------------\n")

#x(5,6) = 5*6
x = lambda a, b : a * b
print(x(5, 6))
print("--------------------------------------------\n")

#myfunc(2): lamda a: a * 2
#mydouble(11) : 11 *2
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
print("--------------------------------------------\n")

#return x*x 
def square(x): 
    return x*x
print([square(x) for x in range(10)])
print("--------------------------------------------\n")

print([(lambda x: x*x)(x) for x in range(10)])

print("--------------------------------------------\n")
print([lambda x: x*x for x in range(10)])

#Iterator
