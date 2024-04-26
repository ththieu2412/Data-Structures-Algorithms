class Node:
    def __init__(self, heSo, soMu):
        self.heSo = heSo
        self.soMu = soMu
        self.keTiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    #bai1
    def them(self, heSo, soMu):
        new_node = Node(heSo, soMu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.keTiep:
                current = current.keTiep
            current.keTiep = new_node
    #bai2
    def rutGon(self):
        if self.head is None:
            return

        current = self.head
        tmp = None  #Xử lý hệ số 0

        while current:
            pre = current
            next_node = current.keTiep
            
            while next_node:
                if current.soMu == next_node.soMu:
                    current.heSo += next_node.heSo
                    pre.keTiep = next_node.keTiep
                    next_node = next_node.keTiep
                else:
                    pre = next_node
                    next_node = next_node.keTiep

            if current.heSo == 0:
                if current == self.head:
                    self.head = current.keTiep
                else:
                    tmp.keTiep = current.keTiep
                deleteNode = current
                current = current.keTiep
                deleteNode = None
            else:
                tmp = current
                current = current.keTiep
                
    #bai3
    def cong(self, daThuc2):
        cur = daThuc2.head
        while cur:
            self.them(cur.heSo,cur.soMu)
            cur = cur.keTiep
        self.rutGon()

    #bai4
    def doiDau(self):
        cur = self.head
        while cur:
            cur.heSo = -cur.heSo
            cur = cur.keTiep 

    #bai5
    def tich(self, daThuc2):
        self.rutGon()
        daThuc2.rutGon()
        ketQua = DaThuc()
        cur1 = self.head
        while cur1:
            cur2 = daThuc2.head
            while cur2:
                ketQua.them(cur1.heSo * cur2.heSo, cur1.soMu + cur2.soMu)
                cur2 = cur2.keTiep
            cur1 = cur1.keTiep
        return ketQua

    #bai6
    def chep(self):
        cur = self.head
        copy_daThuc = DaThuc()
        while cur:
            copy_daThuc.them(cur.heSo,cur.soMu)
            cur = cur.keTiep
        return copy_daThuc


    def inDaThuc(self):
        current = self.head
        while current:
            if current.keTiep:
                print(f"{current.heSo}x^{current.soMu} +", end=" ")
            else:
                print(f"{current.heSo}x^{current.soMu}", end=" ")
            current = current.keTiep
        print()

def main():
    daThuc = DaThuc()
    daThuc2 = DaThuc()

    #them đa thức 1
    daThuc.them(2, 3) 
    daThuc.them(3, 2)
    daThuc.them(-2, 3)  
    daThuc.them(5, 4)  
    daThuc.them(-3, 2)

    #Thêm đa thức 2
    daThuc2.them(2, 2)
    daThuc2.them(0, 6)
    daThuc2.them(2, 3)
    daThuc2.them(5, 2)
    daThuc2.them(1, 3)

    print("Đa thức: ")
    daThuc.inDaThuc()
    
    print("Đa thức 1 sau khi đổi dấu: ")
    daThuc.doiDau()
    daThuc.inDaThuc()

    print("Đa thức 2: ")
    daThuc2.inDaThuc()
    daThuc2.rutGon()
    print("Đa thức 2 sau khi rút gọn")
    daThuc2.inDaThuc()
    daThuc.cong(daThuc2)
    print("Đa thức + đa thức 2: ", end="")
    daThuc.inDaThuc()


    print("Tích hai đa thức: ",end="")
    tich = DaThuc()
    tich = daThuc.tich(daThuc2)
    tich.inDaThuc()

    print("Đa thức copy: ")
    copy_daThuc = daThuc2.chep()
    copy_daThuc.inDaThuc()

if __name__ == "__main__":
    main()
