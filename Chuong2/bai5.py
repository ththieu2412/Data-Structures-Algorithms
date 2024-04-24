def Cong(a, b):
    num_a = int(''.join(map(str,a)))
    num_b = int(''.join(map(str,b)))
    
    result = num_a + num_b

    max_int = 2**31 - 1
    return result if max_int > result else [-1] * len(a)

def main():
    l1 = [2,3,4]
    l2 = [9,1,2]
    print(Cong(l1,l2))

if __name__ == "__main__":
    main()