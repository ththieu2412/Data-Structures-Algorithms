def problem(lt1,lt2):
    result = []
    index_received = []
    index = 0
    for i in lt1:
        for j in lt2:
            if i == j and index not in index_received:
                result.append(i)
                index_received.append(index)
                break
            index += 1
    print(index_received)
    return result

def main():
    num_list1 = [4,9,5,4]
    num_list2 = [4,9,8,4]
    print(problem(num_list1,num_list2))

if __name__ == "__main__":
    main()