class Graph:
    #V là số lượng đỉnh của đồ thị
    def __init__(self,V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        # self.adj[]

    #In theo danh sách cạnh
    def printGraph(self):
        for v in range(self.V):
            print(v," : ",self.adj[v])

    def DFS(self, u, visited):
        visited[u] = True
        for v in self.adj[u]:
            if not visited[v]:
                self.DFS(v, visited)

    def lienThong(self):
        visited = [False] * self.V
        self.DFS(0,visited)

        #Kiểm tra các phần tử có được duyệt hết?
        for i in range(self.V):
            if not visited[i]:
                return False
            
        return True

    def soThanhPhan(self):
        visited = [False] * self.V
        count = 0
        for i in range(self.V):
            if not visited[i]:
                self.DFS(i,visited)
                count += 1
        return count

    #Check bằng DFS
    #Kiểm tra xem 1 đỉnh có chu trình?
    def checkChuTrinh(self, u, visited, par):
        visited[u] = True
        
        for v in self.adj[u]:
            if not visited[v]:
                if self.checkChuTrinh(v,visited,u):
                    return True
            elif v != par:
                return True
        
        return False
    #Kiểm tra đồ thị có chu trình?
    def chuTrinh(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.checkChuTrinh(i,visited,-1):
                    return True
        return False
        
    def bacDinh(self,v):
        result = len(self.adj[v]) 
        return result

    def duongDi(self, v1, v2):
        visted = [False] * self.V
        self.DFS(v1, visted)
        if visted[v2]:
            return True
        return False

def main():
    # g = Graph(5)

    # # Thêm các cạnh vào đồ thị
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(1, 3)
    # g.addEdge(2, 4)
    # g.addEdge(3, 4)

    g = Graph(5)

    # Thêm các cạnh vào đồ thị
    g.addEdge(0, 1)
    g.addEdge(4, 3)
    g.addEdge(2, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.printGraph()

    #Kiểm tra liên thông
    print("Kiểm tra liên thông? ")
    print(g.lienThong())

    #Số thành phần liên thông
    print("Số thành phần liên thông: ", g.soThanhPhan())

    #Kiểm tra chu trình
    print("Đồ thị có chu trình? ", g.chuTrinh())

    #Bậc đinh
    n = 4
    if n > g.V or n < 0:
        raise ValueError("Đỉnh không hợp lệ")
    else:
        print(f"Bậc của đỉnh {n}: {g.bacDinh(n)}")

    #Đường đi
    v1 = 2
    v2 = 4
    if v1 not in range(5) or v2 not in range(5):
        raise ValueError("Đỉnh không hợp lệ")
    else:
        print(g.duongDi(2,4))

    
if __name__ == "__main__":
    main()