def count_chars (string):
    my_dict = {}
    string = string.replace(' ','')
    for i in string:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict

test_string = 'Happiness'
assert count_chars (string = test_string ) == {'H': 1 , 'a': 1 , 'p': 2 , 'i': 1 , 'n': 1 ,
'e': 1 , 's': 2}

string = ' smiles '
print(count_chars(string))