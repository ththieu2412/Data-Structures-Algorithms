def exercise2(path):
    with open(path) as f:
        text = f.read()
        text = text.replace(" ","")
        result = {}
        for i in text:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        return result

def main():
    print(exercise2("test.txt"))

if __name__ == "__main__":
    main()