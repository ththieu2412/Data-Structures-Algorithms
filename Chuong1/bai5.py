def Number(x, y):
    my_dict = {}
    for i in range(x, y+1):
        s = 0
        for j in range(1,i):
            if i%j == 0:
                s += j       
        if s < i:
            my_dict[i] = "deficient"
        elif s == i:
            my_dict[i] = "perfect"
        else:
            my_dict[i] = "abundant"
    return my_dict


while True:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    if x > y:
        print("Enter x < y, please")
    else:
        break

print(Number(x, y))
            

