import numpy as np

def isTrungHang(arr):
    tuple_arr = [tuple(row) for row in arr]
    print(tuple_arr)

    #set khong nhan gia tri trung lao
    return len(arr) != len(set(arr))


def main():
    l1 = [[1,2,3],[5,6,2],[2,6,5]]
    arr1 = np.array(l1)
    print(isTrungHang(arr1))

if __name__ == "__main__":
    main()