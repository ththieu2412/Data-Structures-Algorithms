def isDoiXung(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return False
    return True

n = int(input("Nhap ma tran vuong n = : "))
arr = []
for i in range(n):
    row = []
    for j in range(n):
        print(f"array[{i}][{j}]: ",end="")
        row.append(int(input()))
    arr.append(row)

for i in range(len(arr)):
    print(arr[i])
    
print(isDoiXung(arr))  

