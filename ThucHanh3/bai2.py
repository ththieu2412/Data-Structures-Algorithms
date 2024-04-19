def problem(li1,li2):
    result = []
    index = []
    for i in li1:
        if i in li2 and i not in index:
            result.append(i)
            index.append(i)
    return result


def main():
    my_list = [1,2,3,4,5,5,7,9]
    list = [1,2,3,7,7]
    print(problem(list,my_list))


if __name__ == '__main__':
    main()