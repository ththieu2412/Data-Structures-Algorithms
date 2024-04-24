import numpy as np

def tamGiacDuoi(arr):
    n = arr.shape[0]  # Kích thước của ma trận
    for i in range(n):
        for j in range(i+1,n):  # Chỉ duyệt qua phần bên dưới đường chéo chính
            if arr[i][j] != 0:  # Nếu có một phần tử không bằng 0 ở bên dưới đường chéo chính
                return False
    return True

def main():
    arr = [[1,0,0,0],
           [6,2,0,0],
           [8,5,3,0],
           [8,5,3,0]]
    
    arr = np.array(arr)
    print(tamGiacDuoi(arr))

if __name__ == "__main__":
    main()
