class MyHashSet:

    def __init__(self):
        self.totalKey = 10000
        self.totalBlock = 100
        self.l = [[] for i in range(self.totalKey+1)]
        

    def add(self, key: int) -> None:
        h = key % self.totalKey
        block = key // self.totalBlock
        if len(self.l[h]) == 0:
            self.l[h] = [0 for j in range(self.totalBlock+1)]
        
        self.l[h][block] = 1
        

    def remove(self, key: int) -> None:
        h = key % self.totalKey
        if len(self.l[h]) == 0:
            return
        block = key // self.totalBlock

        self.l[h][block] = 0
        

    def contains(self, key: int) -> bool:
        h = key % self.totalKey
        if len(self.l[h]) == 0:
            return False
        block = key // self.totalBlock
        return self.l[h][block] == 1
        
        

    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)