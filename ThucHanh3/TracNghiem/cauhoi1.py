def max_in_window(num_list, k = 3):
    res = []
    if len(num_list) < k:
        return res
    for i in range(len(num_list)):
        if i + k <= len(num_list):
            res.append(max(num_list[i:i+k]))
    return res

test = [3 , 4 , 5 , 1 , -44]
assert max_in_window(num_list = test , k = 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
print(max_in_window( num_list = num_list , k = 3))