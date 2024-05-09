import array as arr
class a:
    def __init__(self):
        self.a = arr.array('i',[])

    def append(self,value):
        self.a.append(value)

    def show(self):
        for _ in range(len(self.a)):
            print(self.a[_],end=" ")
    
    def duyNhat(self):
        tmp = set(self.a)
        return arr.array('i', tmp)

    def hieu(self, b):
        tmp1 = set(self.duyNhat())
        tmp2 = set(b.a)
        hieu = tmp1 - tmp2     #Lấy phần từ có trong tmp1 mà không có tmp2
        return arr.array('i',sorted(hieu))

    def giao(self, b):
        tmp1 = self.duyNhat()
        tmp2 = b.duyNhat()
        c = arr.array('i',[])
        for i in tmp1:
            if i in tmp2:
                c.append(i)
        return c

    def hop(self, b):
        result = arr.array('i',self.a + b.a)
        return result

def printIterable(iterable):
    for i in iterable:
        print(i,end=" ")

def main():
    #Khởi tạo
    my_array = a()
    my_array.append(12)
    my_array.append(13)
    my_array.append(14)
    my_array.append(15)
    my_array.append(12)
    my_array.append(10)
    my_array.append(12)

    my_array1 = a()
    my_array1.append(12)
    my_array1.append(13)
    my_array1.append(11)
    my_array1.append(16)

    #Duy Nhất
    print("Mảng khởi tạo: ",end=' ')
    my_array.show()
    duy_nhat = my_array.duyNhat()
    print("\nMảng chứa các phần tử không trùng lặp: ", end=" ")
    printIterable(duy_nhat)
    
    #Hieu  
    hieu = my_array.hieu(my_array1)
    print("\nMảng b: ")
    my_array1.show()
    print("\nPhan tu chi co ở mảng ban đầu ma khong co o mảng b: ")
    printIterable(hieu)

    #Giao
    print("\nMảng a: ")
    my_array.show()
    print("\nMảng b: ")
    my_array1.show()
    print("\nGiao giữa mảng a và b: ")
    giao = my_array.giao(my_array1)
    printIterable(giao)

    #Hợp
    print("\n Hợp giữa a và b: ")
    result = my_array.hop(my_array1)
    printIterable(result)

if __name__ == "__main__":
    main()
