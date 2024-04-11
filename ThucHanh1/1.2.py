#create a set
print("create a set")
animals = {"cat", "dog", "tiger"}

print(type(animals))
print(animals)

# create a set
print("create a set")
a_set = {"cat", 5, True, 40.0}

print(type(a_set))
print(a_set)

print("----------------------------")

#No duplication
print("No duplication")
animals = {"cat", "dog", "tiger"}
print(animals)

animals.add("cat")
print(animals)

print("----------------------------")

#copy
print("copy")
animals = {"cat", "dog", "tiger"}
print("Animals:", animals)

a_copy = animals.copy()
print("Copy:", a_copy)
print("----------------------------")
# accessing items
print("accessing items")
animals = {"cat", "dog", "tiger"}
for animal in animals:
    print(animal)
print("----------------------------")
# add an item
print("add an item")
animals = {"cat", "dog", "tiger"}
animals.add("bear")
print(animals)
print("----------------------------")
# insert a set to another set
print("insert a set to another set")
animals = {"cat", "dog", "tiger"}
print(animals)
animals.update({"chicken","Duck"})
print("after use update()")
print(animals)
print("----------------------------")
# join two sets
print("join two sets")
set1 = {"cat", "dog"}
print("set1:", set1)
set2 = {"duck", "tiger"}
print("set2: ", set2)

set3 = set1.union(set2)
print(set3)
print("----------------------------")
# remove an item
print("remove an item")
animals = {"cat", "dog", "tiger"}
print(animals)
animals.remove("dog")
print("after remove")
print(animals)


print("----------------------------")
# discard an item
print("discard an item")
animals = {"cat", "dog", "tiger"}
print(animals)
animals.discard("tiger")
print("after discard")
print(animals)
print("----------------------------")
print("discard an item not in set")
animals = {"cat", "dog", "tiger"}
print(animals)
animals.discard("duck")
print("after discard 'duck'")
print(animals)
print("----------------------------")
# difference 
print("difference between 2 set:")

set1 = {"apple", "banana", "cherry"}
print("set1:", set1)
set2 = {"pineapple", "apple"}
print("set2:", set2)

set3 = set1.difference(set2)
print("difference:", set3)
print("----------------------------")
#toán tử
# AND (&)
print("and(&)")
set1 = {1, 2, 3}
print("set1", set1)

set2 = {3, 4, 5}
print("set2", set2)

print("set1 & set2", set1 & set2)
print("----------------------------")
# OR (|)
print("or(|)")
set1 = {1, 2, 3}
print("set1", set1)
set2 = {3, 4, 5}
print("set2", set2)
print("set1 | set2: ", set1 | set2)
print("----------------------------")
# XOR (^)
print("XOR (^)")
set1 = {1, 2, 3}
print("set1", set1)
set2 = {3, 4, 5}
print("set2", set2)

print("set1 ^ set2: ", set1 ^ set2)
print("----------------------------")
# subtraction (-)
print("subtraction")
set1 = {1, 2, 3}
print("set1", set1)
set2 = {3, 4, 5}
print("set2", set2)
print("----------------------------")
print("set1 - set2: ", set1 - set2)
# set comprehension
print("set comprehension")
aSet = {i*i for i in range(10)}
print(aSet)
print("----------------------------")

#Conversion
# convert from set to list
print("convert from set to list")
aSet = {1, 2, 3, 4, 5}
print(aSet)
aList = list(aSet)
print("List: ",aList)
print(type(aList))

# convert from set to tuple
print("convert from set to tuple")
aSet = {1, 2, 3, 4, 5}
print(aSet)
aTuple = tuple(aSet)
print("Tuple: ",aTuple)
print(type(aTuple))

# convert from tuple to set
print("convert from tuple to set")
aTuple = (1, 2, 3, 2, 1)
print(aTuple)
aSet = set(aTuple)
print("Set: ", aSet)
print(type(aSet))


#Application

# kết nối với file
a_file = open('data.txt','r') 

# read content
data = a_file.read()
print(data)

# Đóng kết nối với file
a_file.close()

#replace

data = data.replace('.', '')
print(data)

data = data.replace(',', '')
print(data)

data = data.replace('-', ' ')
print(data)

#lower
data = data.lower()
print(data)

#split
data = data.split()
print(data)
print(len(data))

#set
data = set(data)
print(data)
print(len(data))

#dictionary
for index, value in enumerate(data):
  print(index, value)