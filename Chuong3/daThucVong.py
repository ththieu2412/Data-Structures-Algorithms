#head -> ... -> tail -> head
class Node:
    def __init__(self, heSo, soMu):
        self.heSo = heSo
        self.soMu = soMu
        self.next = None


class DaThuc:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    #bai1
    def them(self, heSo, soMu):
        newNode = Node(heSo, soMu)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.tail.next = self.head

        
            

    #bai2
    def rutGon(self):
        if self.isEmpty():
            return

        current = self.head
        tmp = None

        while True:
            pre = current
            next_node = current.next

            while True:
                if current.soMu == next_node.soMu:
                    current.heSo += next_node.heSo
                    pre.next = next_node.next
                    next_node = next_node.next
                    if next_node == self.head:  # Đảm bảo không gây ra vòng lặp vô hạn
                        break
                else:
                    pre = next_node
                    next_node = next_node.next
                    if next_node == self.head:  # Đảm bảo không gây ra vòng lặp vô hạn
                        break

            if current.heSo == 0:
                if current == self.head:
                    self.head = current.next

                if tmp:
                    tmp.next = current.next
                else:
                    self.head = current.next  # Cập nhật lại head nếu node đầu bị xóa
                deleteNode = current
                current = current.next
                deleteNode = None
                if current == self.head:  # Kiểm tra nếu danh sách chỉ có một node
                    break
            else:
                tmp = current
                current = current.next
                if current == self.head:  # Đảm bảo không gây ra vòng lặp vô hạn
                    break

            
                
    
    # #bai3
    # def cong(self, daThuc2):
    #     cur = daThuc2.head
    #     while cur:
    #         self.them(cur.heSo,cur.soMu)
    #         cur = cur.keTiep
    #     self.rutGon()

    # #bai4
    # def doiDau(self):
    #     cur = self.head
    #     while cur:
    #         cur.heSo = -cur.heSo
    #         cur = cur.keTiep 

    # #bai5
    # def tich(self, daThuc2):
    #     self.rutGon()
    #     daThuc2.rutGon()
    #     ketQua = DaThuc()
    #     cur1 = self.head
    #     while cur1:
    #         cur2 = daThuc2.head
    #         while cur2:
    #             ketQua.them(cur1.heSo * cur2.heSo, cur1.soMu + cur2.soMu)
    #             cur2 = cur2.keTiep
    #         cur1 = cur1.keTiep
    #     return ketQua

    # #bai6
    # def chep(self):
    #     cur = self.head
    #     copy_daThuc = DaThuc()
    #     while cur:
    #         copy_daThuc.them(cur.heSo,cur.soMu)
    #         cur = cur.keTiep
    #     return copy_daThuc


    def inDaThuc(self):
        current = self.head
        if self.isEmpty():
            print("Danh sách rỗng")
        else:
            while True:
                if current.next != self.head:
                    print(f"{current.heSo}x{current.soMu} + ",end=" ")
                else:
                    print(f"{current.heSo}x{current.soMu}",end=" ")
                current = current.next
                if current == self.head:
                    break


def main():
    daThuc = DaThuc()
    daThuc2 = DaThuc()

    #them đa thức 1
    daThuc.them(2, 3) 
    daThuc.them(3, 2)
    daThuc.them(0, 3)  
    daThuc.them(5, 4)  
    daThuc.them(-3, 2)
    daThuc.rutGon()
    daThuc.inDaThuc()
    # #Thêm đa thức 2
    # daThuc2.them(2, 2)
    # daThuc2.them(0, 6)
    # daThuc2.them(2, 3)
    # daThuc2.them(5, 2)
    # daThuc2.them(1, 3)

    # print("Đa thức: ")
    # daThuc.inDaThuc()
    
    # print("Đa thức 1 sau khi đổi dấu: ")
    # daThuc.doiDau()
    # daThuc.inDaThuc()

    # print("Đa thức 2: ")
    # daThuc2.inDaThuc()
    # daThuc2.rutGon()
    # print("Đa thức 2 sau khi rút gọn")
    # daThuc2.inDaThuc()
    # daThuc.cong(daThuc2)
    # print("Đa thức + đa thức 2: ", end="")
    # daThuc.inDaThuc()


    # print("Tích hai đa thức: ",end="")
    # tich = DaThuc()
    # tich = daThuc.tich(daThuc2)
    # tich.inDaThuc()

    # print("Đa thức copy: ")
    # copy_daThuc = daThuc2.chep()
    # copy_daThuc.inDaThuc()

if __name__ == "__main__":
    main()
