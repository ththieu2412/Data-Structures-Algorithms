class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class dslk:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head is None

    def append(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def daoNguoc(self):
        if self.isEmpty():
            return None
        else:
            current = self.head
            previous = None
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            self.head = previous
 
    def inDanhSach(self):
        if self.isEmpty():
            return None
        else:
            current = self.head
            while current:
                if current.next is not None:
                    print(f"{current.info} -> ",end="")
                else:
                    print(f"{current.info} -> None",end="")
                current = current.next
    
    def inNguoc(self):
        if self.isEmpty():
            return None
        else:
            stack = []
            cur = self.head
            while cur:
                stack.append(cur.info)
                cur = cur.next
            
            while stack:
                print(f"{stack.pop()} -> ",end="")
    
    def inNguocDeQui(self, node):
        if node is None:
            return node
        self.inNguocDeQui(node.next)
        print(f"{node.info} -> ", end="")


link_listed = dslk()
link_listed.append(1)
link_listed.append(2)
link_listed.append(3)
link_listed.append(4)
link_listed.append(5)
link_listed.append(6)
print("Danh sach ban dau: ")
link_listed.inDanhSach()
print("\nIn ngược danh sách: ")
link_listed.inNguocDeQui(link_listed.head)
print("\nDanh sách sao khi đảo ngược")
link_listed.daoNguoc()
link_listed.inDanhSach()
