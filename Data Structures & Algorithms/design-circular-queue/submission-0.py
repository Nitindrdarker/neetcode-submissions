class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for i in range(k)]
        self.start = 0
        self.end = -1
        self.k = k

        

    def enQueue(self, value: int) -> bool:
        if (self.isFull()):
            return False
        
        self.end = (self.end + 1)
        self.q[self.end % self.k] = value
        print(self.q)
        return True
        

    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False
        self.q[self.start % self.k] = -1
        self.start = (self.start + 1)
        return True

    def Front(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.q[self.start % self.k]
        

    def Rear(self) -> int:
        print(self.q, self.isEmpty())
        if (self.isEmpty()):
            return -1
        
        return self.q[self.end % self.k]
        

    def isEmpty(self) -> bool:
        return self.end < self.start
        

    def isFull(self) -> bool:
        return self.end - self.start + 1 == self.k



        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()