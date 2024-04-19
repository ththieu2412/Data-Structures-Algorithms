import bai3

def countCharsFile(path):
    with open(path, 'r') as f:
        str = f.read()
        res = bai3.count_chars(str)
        return res

def main():
    print(countCharsFile("test.txt"))

if __name__ == '__main__':
    main()

data = "I’m learning Python!"
print(data.split())



        
