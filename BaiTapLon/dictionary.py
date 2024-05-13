class Nghia:
    def __init__(self, loai_tu, phan_nghia, vi_du):
        self.loai_tu = loai_tu
        self.phan_nghia = phan_nghia
        self.vi_du = vi_du

#Một từ có thể chứa nhiều nghĩa
class TuVung:
    def __init__(self, tu_vung):
        self.tu_vung = tu_vung
        self.nghia = []

class TuDienAnhAnh:
    def __init__(self):
        self.danh_sach = []

    def themTuVung(self, tu_vung, loai_tu, phan_nghia, vi_du):
        nghia_moi = Nghia(loai_tu, phan_nghia, vi_du)
        index = 0           #Lưu vị trí từ cần thêm
        for i, j in enumerate(self.danh_sach):
            if j.tu_vung > tu_vung:
                index = i
                break
            elif j.tu_vung == tu_vung:
                j.nghia.append(nghia_moi)
                return
            index += 1
        tu_vung_moi = TuVung(tu_vung)
        tu_vung_moi.nghia.append(nghia_moi)

        #Lưu từ vựng mới vào từ điển
        self.danh_sach.append(tu_vung_moi)
    
    def remove(self, word):
        for i in self.danh_sach:
            if i.tu_vung == word:
                self.danh_sach.remove(i)
                return True
        return False

    def traCuu(self, tu_vung):
        for tu in self.danh_sach:
            if tu_vung == tu.tu_vung:
                return tu.nghia
        return None

    def luuFile(self, file_name):
        with open(file_name,'w') as f:
            for i in self.danh_sach:
                f.write(i.tu_vung + "\n")
                for meaning in i.nghia:
                    f.write(meaning.loai_tu + ' : ' + meaning.phan_nghia + '\n')
                    f.write("Example: " + meaning.vi_du + "\n")
                f.write('\n')

    def loadFile(self, file_name):
        self.danh_sach.clear()  # Clear existing data before loading
        with open(file_name, 'r') as f:
            lines = f.readlines()
            word = None
            meaning1 = None
            for line in lines:
                line = line.strip()  
                if line:  # Non-empty line
                    if not word:
                        word = TuVung(line)
                    elif not meaning1:
                        meaning1 = line.split(" : ")
                    else:
                        example = line.split("Example: ")[-1]  
                        word.nghia.append(Nghia(meaning1[0], meaning1[1], example))
                        meaning1 = None  #Trả về giá None khi đã có nghĩa
                else:  
                    if word:
                        for i in word.nghia:
                            self.themTuVung(word.tu_vung, i.loai_tu, i.phan_nghia, i.vi_du)
                        word = None  
        print("Load successful")


                


def main():
    tu_dien = TuDienAnhAnh()
    flag = True
    while flag:
        print("=====================DICTIONARY========================")
        print("1. Add a new entry to the dictionary.")
        print("2. Remove a dictionary entry.")
        print("3. Look up the definition of a word in the dictionary")
        print("4. Save dictionaries to files")
        print("5. Load dictionaries from files")
        print("6. Exit")
        print("========================================================")
        
        t = True
        while t:
            n = input("Your chose: ")
            if not n.isdigit():
                print("Invalid input. Please enter a number")
            else:
                n = int(n)
                t = False

        if n == 1:
            new_word = input("Enter new vocabulary: ")
            tu_loai = input("Part of word: ")
            nghia = input("Meaning: ")
            vi_du = input("Example: ")

            tu_dien.themTuVung(new_word, tu_loai, nghia, vi_du)
            print("Add successful")

        elif n == 2:
            word = input("Enter vocabulary to remove: ")
            if tu_dien.remove(word):
                print("Remove successful")
            else:
                print("Not vocabulary found")

        elif n == 3:
            word = input("Enter vocabulary to look up: ")
            nghia = tu_dien.traCuu(word)
            if nghia:
                print(f"Meaning of '{word}':")
                for i in nghia:
                    print(f"{i.loai_tu} : {i.phan_nghia}")
                    print(f"Example: {i.vi_du}")
            else:
                print("No vocabulary found")
        
        elif n == 4:
            file_name = "N21DCCN122_mang"
            tu_dien.luuFile(f"./BaiTapLon/{file_name}")
            print("Save successful")
       
        elif n == 5:
            file_name = "N21DCCN122_mang"
            tu_dien.loadFile(f"./BaiTapLon/{file_name}")
        else:
            flag = False

    print("See you again")
    

if __name__ == "__main__":
    main()