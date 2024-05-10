class DoThiCoHuong:
    def __init__(self, v):
        self.V = v
        self.adj = [[] for _ in range(self.V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)

    def inDanhSachCanh(self):
        for v in range(self.V):
            print(v, " : ", self.adj[v])

    def soCungVao(self, v):
        count = 0
        for i in self.adj:
            if v in i:
                count += 1
        return count
        
    def soCungRa(self, u):
        result = len(self.adj[u])
        return result
    

g = DoThiCoHuong(5)

# Thêm các cạnh vào đồ thị
g.themCanh(0, 1)
g.themCanh(4, 3)
g.themCanh(2, 4)
g.themCanh(1, 2)
g.themCanh(2, 3)

g.inDanhSachCanh()
print("Số cung vào: ", g.soCungVao(4))
print("Số cung ra: ", g.soCungRa(2))