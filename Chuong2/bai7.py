def Nhan(a, b):
    num_a = int(''.join(map(str,a)))
    num_b = int(''.join(map(str,b)))
    
    result = num_a * num_b

    max_int = 2**31 - 1

    return result if result < max_int else [-1] * len(a)
    
def main():
    l1 = [9,8,9,6,9,6,9,2,3,4]
    l2 = [9,1,2]
    print(Nhan(l1, l2))

if __name__ == "__main__":
    main()