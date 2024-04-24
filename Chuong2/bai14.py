def DayConDauTien(a, b):
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == a[j]:

                # Kiểm tra phần tử liên tiếp bắt đầu từ vị trí j, j
                tmp_a = i
                tmp_b = j
                while tmp_a < len(a) and tmp_b < len(b) and a[tmp_a] == b[tmp_b]:
                    result.append(a[tmp_a])
                    tmp_a += 1
                    tmp_b += 1
                
                if len(result) > 1:
                    return result
                else:
                    result = []
  
    return result


a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
print(DayConDauTien(a, b)) 
