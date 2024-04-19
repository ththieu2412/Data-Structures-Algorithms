def count_chars(string):
    my_dict = {}
    string = string.replace(' ','')
    for i in string:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict

def main():
    my_string = "Happiness"
    print(count_chars(my_string))

if __name__ == "__main__":
    main()