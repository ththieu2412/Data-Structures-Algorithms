import numpy as np

def isTamGiacTren(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i,j] != 0:
                return False
    return True

def main():
    l1 = [[1,2,3],[4,5,6],[7,7,9]]
    l2 = [[1,2,3],[0,5,6],[0,0,9]]
    arr1 = np.array(l1)
    arr2 = np.array(l2)
    print(isTamGiacTren(arr1))
    print(isTamGiacTren(arr2))

if __name__ == "__main__":
    main()


