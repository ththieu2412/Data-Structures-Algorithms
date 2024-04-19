def slidingWindow(li, k):
    res = []
    if len(li) < k:
        return res
    for i in range(len(li)):
        if i + k <= len(li):
            res.append(max(li[i:i+k]))
    return res

def main():
    my_list = [3,4,5,1,-44,5,10,12,33,1]
    k = 3
    print(slidingWindow(my_list,k))

if __name__ == '__main__':
    main()