import numpy as np

def trungCot(arr):
    n = arr.shape[0]
    lst = []
    for i in range(n):
        column = []
        for j in range(n):
            column.append(arr[j][i])
        lst.append(column)
    return len(lst) != len(set(map(tuple,lst)))
                

def main():
    arr1 = [[1,0,0,1],
           [6,2,0,6],
           [8,5,3,8],
           [8,5,3,8]]
    
    arr2 = [[1,0,0,0],
           [6,2,0,0],
           [8,5,3,0],
           [8,5,3,0]]
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    print(trungCot(arr1))
    print(trungCot(arr2))
    

if __name__ == "__main__":
    main()