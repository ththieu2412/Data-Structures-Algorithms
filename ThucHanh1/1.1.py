#Tuple

#Để tạo một tuple, đặt các giá trị trong ngoặc
t = (1,2,3)

print("Để tạo một tuple, đặt các giá trị trong ngoặc")
print(t[0])
print(t[1])
print(t[2])
print("----------------------------------------\n")

#Cũng có thể tạo một tuple không có dấu ngoặc đơn, bằng cách sử dụng dấu phẩy
print("Cũng có thể tạo một tuple không có dấu ngoặc đơn, bằng cách sử dụng dấu phẩy")
t = 1 , 2
print(t)
print(type(t))
print("----------------------------------------\n")

#Nếu bạn muốn tạo một tuple với một phẩn tử duy nhất, bạn phải sử dụng dấu phẩy
print("Nếu bạn muốn tạo một tuple với một phẩn tử duy nhất, bạn phải sử dụng dấu phẩy")
singleton = (1,)
print(singleton)

var1 = (1 + 2) * 5
print(type(var1), ' ', var1)

var2 = (1)
print(type(var2),' ', var2)

var3 = (1, )
print(type(var3), ' ', var3)
print("----------------------------------------\n")

#Lặp lại tuple bằng cách nhân tuple với một số
print("Lặp lại tuple bằng cách nhân tuple với một số")
t = (1,) * 6
print(t)
print("----------------------------------------\n")

#Nối các bộ dữ liệu và sử dụng phép gán tăng giá trị
print("Nối các bộ dữ liệu và sử dụng phép gán tăng giá trị")
t1 = (1, 0)
print(t1)

t1 += (2,)
print(t1)
print("----------------------------------------\n")

#Methods
print("Tuple Method")
t = (1,2,3,1)
count = t.count(1)
index = t.index(2)

print(count)
print(index)
print("----------------------------------------\n")

#Interests Of Tuples
#Tuple cặp khóa/ giá trị để xây dựng dictionary
print("Tuple cặp khóa/ giá trị để xây dựng dictionary")
d = dict([('jan',1),('feb',2),('march',3)])
print(d['jan'])
print(d['feb'])
print(d['march'])
print("----------------------------------------\n")

#Get multiple values
print("Get multiple values")
x1,y1,z1   = ('a','b','c')
(x2,y2,z2) = ('a','b','c')
(x3,y3,z3) = range(3)

print(x1)
print(x2)
print(x3)
print("----------------------------------------\n")

d = {'first':'string value', 'second':1}
for a in d:
    print(a)
print("----------------------------------------\n")

d = {'first':'string value', 'second':[1,2]}
items = d.items()
print('items:', items)
for k,v in items:
    print(k, v)
print("----------------------------------------\n")

#Tuple Unpacking
print("Tuple unpacking cho phép trích xuất các phần tử tuple tự động là danh sách các biến ở bên trái có cùng số phần tử với độ dài của tuple")
data = (1,2,3)
x, y , z = data
print(x)
print("----------------------------------------\n")

#Swap Function
print("Swap Function")
x = 4
y = 5

print(x, y)

#(x,y) = (y,x)
x,y = y,x
print(x, y)
print("----------------------------------------\n")

#Misc
#Length
print("Length of Tuple")
t = (1,2,3,4)
print(len(t))
print("----------------------------------------\n")

#Slicing
print("Slicing")
data = (1, 2, 3, 4, 5)
print(data[2:])
print(data[::-1])
print("----------------------------------------\n")

#Tuple are not fully immutable
print("Tuple are not fully immutable")
t = (1, 2, [3, 10])
t[2][0] = 9
print(t)
print("----------------------------------------\n")

#Error
# t = (1, 2, 3, 4, 5)
# t[2] = 9
# print(t)

#Chuyển đổi tuple thành chuỗi
print("Chuyển đổi tuple thành chuỗi")
data = (1, 2, 3, 4, 5)
data_str = str(data)
print(data_str)
print(type(data_str))
print(data_str[0])
print("----------------------------------------\n")

#Toán tử so sánh và các hàm số học
print("#Toán tử so sánh và các hàm số học")
t = (1, 2, 3, 4, 5)

print(min(t))
print(max(t))
print(sum(t))
print("----------------------------------------\n")

#Sắp xếp tuple theo thứ tự tăng dần
t = (4, 7, 3, 9, 6)
t_s = sorted(t)
print(t_s)
print("----------------------------------------\n")

#Gộp theo cặp 2 tuple
t1 = (1, 2, 3, 4, 5)
t2 = ('a', 'b', 'c', 'd', 'e')

print(t1)
print(t2)

t3 = zip(t1, t2)
for x,y in t3:
    print(x, y)
print("----------------------------------------\n")

#Giải phương trình bậc 2
import math

def quadratic_equation(a, b, c):
    '''
    This function aims at solving the quadratic equation
    a, b, c --- three parameters and a =! 0
    '''
    
    # compute delta
    delta = b*b - 4*a*c

    if delta < 0:
        return ()
    elif delta == 0:
        x = (-b+math.sqrt(delta))/2*a
        return (x,)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return (x1,x2)

#delta < 0
result = quadratic_equation(a=5, b=0, c=1)
print(type(result))
print(len(result))
print(result)
print("----------------------------------------\n")

#delta > 0
result = quadratic_equation(a=5, b=5, c=1)
print(type(result))
print(len(result))
print(result)
print("----------------------------------------\n")

#delta = 0
result = quadratic_equation(a=4, b=4, c=1)
print(type(result))
print(len(result))
print(result)
print("----------------------------------------\n")

# tuple and zip
x_data = [1, 2, 3]
y_data = [5, 6, 7]
data = zip(x_data, y_data)

# print
for d in data:
    print(d)
    print(type(d))
print("----------------------------------------\n")

#Tuple and List
# memory comparison
print("memory comparison")
import sys

aList  = [3, 4, 5, 6, 7]
aTuple = (3, 4, 5, 6, 7)

print(sys.getsizeof(aList))
print(sys.getsizeof(aTuple))
print("----------------------------------------\n")

# convert from list to tuple
print("convert from list to tuple")
aList  = [3, 4, 5, 6, 7]
aTuple = tuple(aList)

print(aTuple)
print(type(aTuple))
print("----------------------------------------\n")

# convert from tuple to list
print("Convert from tuple to list")
aTuple  = (3, 4, 5, 6, 7)
aList = list(aList)

print(aList)
print(type(aList))
print("----------------------------------------\n")
