import numpy as np

def isTrungHang(arr):
    tuple_arr = [tuple(row) for row in arr]

    #set khong nhan gia tri trung lao
    return len(tuple_arr) != len(set(tuple_arr))


def main():
    l1 = [[1,2,3],[5,6,2],[2,6,5]]
    arr1 = np.array(l1)
    print(isTrungHang(arr1))

if __name__ == "__main__":
    main()