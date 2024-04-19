def intersection (lst1 , lst2):
    result = []
    index = []
    for i in lst1:
        if i in lst2 and i not in index:
            result.append(i)
            index.append(i)
    return result

test_list1 = [4 , 9]
test_list2 = [9 , 2]
assert intersection (lst1 = test_list1 , lst2 = test_list2 ) == [9]

num_list1 = [4 , 9 , 5]
num_list2 = [9 , 4 , 9 , 8 , 4]
print(intersection(num_list1 , num_list2))