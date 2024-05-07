class HanoiTower:
    def __init__(self, n):
        self.n = n

    def move(self, n, tower1, tower2, tower3):
        if n == 1:
            print(f"Chuyển đĩa {n} từ {tower1} sang {tower3}")
            return
        else:
            self.move(n-1,tower1,tower3,tower2)
            print(f"Chuyển đĩa {n} từ {tower1} sang {tower3}")
            self.move(n-1,tower2,tower1,tower3)
        
        


n = 3  
hanoiTower = HanoiTower(n)
hanoiTower.move(3,"Tower1","Tower2","Tower3")
