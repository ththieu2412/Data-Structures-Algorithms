#Khởi tạo

keys   = ['a', 'b', 'c']
values = [1, 2, 3]

a_dictionary = {(k,v) for (k,v) in zip(keys,values)}
print(a_dictionary)
print(type(a_dictionary))

parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

print(parameters)
print(type(parameters))

parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

keys   = parameters.keys()
print(keys)

#keys
for key in keys:
  print(key)

#values
values = parameters.values()
for value in values:
    print(value)


#items
parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}
items = parameters.items()
for key, value in items:
  print(key, value)

parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

for key in parameters:
  print(key)


#get
parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

value = parameters.get('learning_rate')
print(value)

print('\nAfter using get() function')
print(parameters)

#pop
parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

value = parameters.pop('learning_rate')
print(value)

print('\nAfter using pop() function')
print(parameters)

#get when key not in dict
parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

value = parameters.get('algorithm')
print(value)


#popitem
parameters = {'learning_rate': 0.1,
  'optimizer': 'Adam',
  'metric': 'Accuracy'}

item = parameters.popitem()

print(item)
print(parameters)

#clear
parameters = {'learning_rate': 0.1,
  'metric': 'Accuracy'}

print('Before using clear() function')
print(parameters)

parameters.clear()

print('\nAfter using clear() function')
print(parameters)

#copycopy
parameters = {'learning_rate': 0.1,
  'metric': 'Accuracy'}

a_copy = parameters.copy()
a_copy['learning_rate'] = 0.2

print(parameters)
print(a_copy)

#insert
parameters = {'learning_rate': 0.1,
  'metric': 'Accuracy'}

parameters['learning_rate'] = 0.2
print(parameters)

d = {'first':'string value', 'second':[1,2]}
keys = d.keys()
values = d.values()

print(keys)
print(values)

#truy cập giá trị của một khóa đã cho
d = {'first':'string value', 'second':[1,2]}
print(d['first'])
print(d['second'])


#phương pháp truy vấn thông tin
d = {'first':'string value', 'second':[1,2]}
items = d.items()

print('items:', items)
for k,v in items:
    print(k, v)

d = {'first':'string value', 'second':[1,2]}
value = d.get('first')

print(value)
print(d)

d = {'first':'string value', 'second':[1,2]}
value = d.pop('first')

print(value)
print(d)

#popitem loại bỏ và trả về 1 cặp (key, value)
d = {'1':'value1', '2':'value2', '3':'value3', '4':'value4'}
item = d.popitem()

print(item)
print(d)

#Để tạo 1 đối tượng mới sử dụng phương thức sao chép 
d1 = {'a': [1,2]}
d2 = d1.copy()

print('d1:', d1)
print('d2:', d2)

# thay đổi giá trị d2 sẽ ảnh hưởng đến d1
d1 = {'a': [1,2], 'b': 5}
d2 = d1.copy()

d2['a'][0] = 3
d2['a'][1] = 4

print('d1:', d1)
print('d2:', d2)

#deepcopy, khi thay đổi d2 thì d1 không bị ảnh hưởng
import copy
d1 = {'a': [1,2], 'b': 5}
d2 = copy.deepcopy(d1)

# thay đổi giá trị d2 
d2['a'][0] = 3
d2['a'][1] = 4

print('d1:', d1)
print('d2:', d2)

#clear xóa tất cả nhưng del () chỉ xóa một
d = {'a':1, 'b':2, 'c':3}
del d['a']
print(d)

d = {'a': [1,2], 'b': 5}
print(d)

del d

#tạo một từ điển cho một bộ khóa
d1 = {'a': [1,2]}
d2 = d1.copy()
d2.fromkeys(['first', 'second'])

#phương thức fromkeys() tạo ra một từ điển mới với các từ khóa đã cho, mỗi khóa có giá trị mặc định là None
{}.fromkeys(['first', 'second'])

#Combining dict

#update
d1 = {'a':1}
d2 = {'b':2, 'c':3}

print('d1:', d1)
print('d2:', d2)

d1.update(d2)
print('d1 sau khi update:', d1)

# #iterators

# t = {'b':2, 'c':3}
# [x for x in t.itervalues()]
# [x for x in t.iterkeys()]
# [x for x in t.iteritems()]

l_keys   = ['a', 'b', 'c', 'd', 'e']
l_values = [1, 2, 3, 4, 5]

d = {(k,v) for (k,v) in zip(l_keys,l_values)}
print(d)

# dic comprehension

aDict = {str(i):i for i in range(5)}
print(aDict)

# from zip

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

a_dict = dict(zip(tuple1, tuple2))
print(type(a_dict))
print(a_dict)

# setdefault()

fruits = {'banana': 2}
fruits.setdefault('apple', 0)

print(fruits)

# setdefault()

fruits = {'banana': 2, 'apple': 4}
fruits.setdefault('apple', 0)

print(fruits)


# setdefault()

fruits = {'banana': 2}
fruits.setdefault('apple', 0)

fruits['apple'] += 10
print(fruits)

# merge two dicts

fruits = {'banana': 2, 'apple': 4}
cereal = {'rice': 3, 'corn': 7}

result = {**fruits, **cereal}
print(result)

# check if a key exists

fruits = {'banana': 2, 'apple': 4}

print('apple' in fruits)
print('corn' in fruits)

# remove empty items

fruits = {'banana': 2, 'apple': None}

dict1 = {key:value for (key, value) 
                     in fruits.items() 
                     if value is not None}
print(dict1)

# access value via key use get

fruits = {'banana': 2, 'apple': 4}
print(fruits.get('apple'))
print(fruits.get('corn'))

# access value via key

fruits = {'banana': 2, 'apple': 4}
print(fruits['apple'])
# print(fruits['corn'])

#dictionary and file

import json

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

with open('data.json', 'w') as fp:
    json.dump(parameters, fp)
with open('data.json', 'r') as fp:
    data = json.load(fp)
print(data)
print(data['learning_rate'])

#iterables and sorting
# create a list
aList = [1, 5, 3, 7, 4]
print(aList)

# sort
sortedList = sorted(aList)
print(sortedList)

# create a list
aList = [1, 5, 3, 7, 4]
print(aList)

# function for sorting
def compare(item):
    return item

# sort
sortedList = sorted(aList, key=compare)
print(sortedList)
print("-------------------")
# data
list1 = [1, 5, 3, 7, 4]
list2 = [16, 13, 18, 11, 15]

# create a dictionary
dictionary = dict(zip(list1, list2))
print(dictionary)

sortedDict = sorted(dictionary)
print(sortedDict)
print("-------------------")

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)

list4 = sorted(list3)
print(list4)
print("-------------------")

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# function for sorting
def compare(item):
    return item[0]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)
list4 = sorted(list3, key=compare)
print(list4)
print("-------------------")

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# function for sorting
def compare(item):
    return item[1]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)
list4 = sorted(list3, key=compare)
print(list4)
print("-------------------")

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)
list4 = sorted(list3, key=lambda item: item[1])
print(list4)