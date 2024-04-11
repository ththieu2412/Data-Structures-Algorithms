import numpy as np

def nhomHang(arr):
    for i in range(len(arr)):
       for j in range(i+1,len(arr)):
           if np.array_equal(arr[i],arr[j]):
                print(f"{i}: {arr[i]}")
                break  #Dừng vòng lặp nếu tìm được vị trí trùng
        


def main():
    l1 = [[1,2,3],[5,6,2],[1,2,3],[1,2,3]]
    arr1 = np.array(l1)
    nhomHang(arr1)

if __name__ == "__main__":
    main()