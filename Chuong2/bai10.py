import numpy as np

def trungCot(arr):
    n = arr.shape[1]
    lst = []
    for i in range(n):
        column = []
        for j in range(n):
            column.append(arr[j][i])
        lst.append(column)

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                print(f"Cột {i} và cột {j} giống nhau: {lst[i]}")

def main():
    arr1 = [[1,1,0,1],
            [6,6,0,6],
            [8,8,3,8],
            [8,8,3,8]]
    
    arr1 = np.array(arr1)
    trungCot(arr1)

if __name__ == "__main__":
    main()
