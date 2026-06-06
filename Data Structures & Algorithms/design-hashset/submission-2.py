class MyHashSet:

    def __init__(self):
        self.totalKey = 10000
        self.totalBlock = 100
        self.l = [[False for j in range(self.totalBlock+1)] for i in range(self.totalKey+1)]
        

    def add(self, key: int) -> None:
        h = key % self.totalKey
        block = key // self.totalBlock
        print(h, block)
        self.l[h][block] = True
        

    def remove(self, key: int) -> None:
        h = key % self.totalKey
        block = key // self.totalBlock
        self.l[h][block] = False
        

    def contains(self, key: int) -> bool:
        h = key % self.totalKey
        block = key // self.totalBlock
        return self.l[h][block] == True
        
        

    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)