def solve(num_list, k):
    s = []
    for i in range(len(num_list)):
        if i + k > len(num_list):
            break
        s.append(max(num_list[i:i+k]))
    return s

def main():
    while True:
        n = int(input("Nhập số phần tử của list: "))
        k = int(input("Nhập k: "))
        if n > k:
            break
        print("Nhập n > k!")

    my_list = [int(input(f"Nhập phần tử thứ {x}: ")) for x in range(n)]
    print(solve(my_list,k))

if __name__ == "__main__":
    main()
