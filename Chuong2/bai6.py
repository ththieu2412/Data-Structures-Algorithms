def Tru(a, b):
    num_a = int(''.join(map(str,a)))
    num_b = int(''.join(map(str,b)))
    
    if(num_a < num_b):
        raise Exception("Nhap mang a >= b!")
    
    result = num_a - num_b
    return result
    
def main():
    l1 = [2,3,4]
    l2 = [9,1,2]
    print(Tru(l1, l2))

if __name__ == "__main__":
    main()