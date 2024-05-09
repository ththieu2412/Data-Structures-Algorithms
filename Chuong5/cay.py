from collections import deque

class Node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
        
    #Gán giá trị node ban đầu là None(=self.root)
    def soNut(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return self.demSoNut(self.root)

    def demSoNut(self, node):
            if node is None:
                return 0
            else:
                return self.demSoNut(node.left) + self.demSoNut(node.right) + 1
            
    def chieuCao(self, node):
        if node is None:
            return 0
        else:
            return max(self.chieuCao(node.left),self.chieuCao(node.right)) + 1


    def soNutLa(self):
        
        def dem(node):
            if node is None:
                return 0
            if node.right is None and node.left is None:
                return 0
            return dem(node.right) + dem(node.left) + 1
        
        return dem(self.root)

    # def preOrder(self,node):
    #     if node is None:
    #         return node
    #     print(node.info," -> ",end="")
    #     self.preOrder(node.left)
    #     self.preOrder(node.right)
        
    def soNutTrungGian(self):
        if self.isEmpty() or self.chieuCao(self.root) <= 1:
            return 0
        return self.soNut() - self.soNutLa() - 1

    def soSanh(self, node1, node2):
        return node1.info < node2.info    
    
    def isBST(self, node):
        return self.checkBST(node, float("-inf"), float("inf"))

    def checkBST(self, node, min_value, max_value):
        if node is None:
            return True
        if node.info <= min_value or node.info >= max_value:
            return False
        return (self.checkBST(node.left, min_value, node.info) and
                self.checkBST(node.right, node.info, max_value))

    def printStructure(self):
        if self.root is None:
            print("Cây rỗng")
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node is not None:
                    print(node.info, end=" ")
                    if node.left is not None or node.right is not None:
                        queue.append(node.left)
                        queue.append(node.right)
            print()  


    def isAVL(self, node):
        if node is None:
            return True
        left_height = self.chieuCao(node.left)
        right_height = self.chieuCao(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isAVL(node.right) and self.isAVL(node.left) 
    
    def chep(self, node):

        if node is None:
            return None
        new_node = Node(node.info)
        new_node.left = self.chep(node.left)
        new_node.right = self.chep(node.right)
        return new_node

    def soSanh(self,cay2):
        return self.soSanhNode(self.root,cay2.root)

    def soSanhNode(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.info != node2.info:
            return False
        return self.soSanhNode(node1.right, node2.right) \
        and self.soSanhNode(node1.left, node2.left)
    
    def search(self, node, value):
        if node is None:
            return None
        elif value > node.info:
            return self.search(node.right,value)
        elif value < node.info:
            return self.search(node.left,value)
        else:
            return node
    
    def cayCon(self,cay2):
        #Tìm vị trí root của cây thứ 2 trong cây thứ 1
        if cay2.isEmpty() or self.isEmpty():
            return False
        tmp = Tree()
        tmp.root = self.search(self.root,cay2.root.info) 
        if tmp is None:
            return False
        
        #So sánh cây 2 với cây có nút gốc là tmp vừa tìm được
        return cay2.soSanh(tmp)                                                                                                                                                                                                        

    def checkCBHT(self, node):
        if node is None:
            return True
        
        left_height = self.demSoNut(node.left)
        right_height = self.demSoNut(node.right)
        
        if abs(left_height - right_height) <= 1:
            return self.checkCBHT(node.right) and self.checkCBHT(node.left)
        else:
            return False
        
    def BSTTuanTu(self):
        if self.root is None:
            return False
        
        def is_sequential(node):
            if node is None:
                return True
            if (node.left is None and node.right is not None) or \
               (node.left is not None and node.right is None):
                return is_sequential(node.left) and is_sequential(node.right)
            else:
                return False
        
        return is_sequential(self.root)
    
cay = Tree()
cay.root = Node(4)
cay.root.left = Node(2)
cay.root.right = Node(6)
cay.root.left.left = Node(1)
cay.root.left.right = Node(3)
cay.root.right.left = Node(5)
cay.root.right.right = Node(7)
print("Cây : ")
cay.printStructure()
print("\nSố nút: ",cay.soNut())
print("Chiều cao: ",cay.chieuCao(cay.root))
print("Số nút lá: ",cay.soNutLa())
print("Số nút trung gian: ", cay.soNutTrungGian())
print("Cây nhị phân? ", cay.isBST(cay.root))  #float("-inf") khởi tạo giá trị âm vô cùng để so sánh
print("Cây cân bằng? ", cay.isAVL(cay.root))  

#Sao Chep
cay_moi = Tree()
cay_moi.root = cay.chep(cay.root)
print("Cây sao chép: ")
cay_moi.printStructure()

#So sánh
print(cay.soSanh(cay_moi))

#Cây con
cay_con = Tree()
cay_con.root = Node(6)
cay_con.root.left = Node(5)
cay_con.root.right = Node(7)
print("Cây con? ")
print(cay.cayCon(cay_con))

#Cân bằng hoàn toàn
print("Cây cân bằng hoàn toàn? ")
print(cay.checkCBHT(cay.root))

#Cây tìm kiếm tuần tự
print(cay.BSTTuanTu())