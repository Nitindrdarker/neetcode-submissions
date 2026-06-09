class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.freqMap = {}
        self.stackList = [[] for i in range(20000)]

        

    def push(self, val: int) -> None:

        self.freqMap[val] = self.freqMap.get(val, 0) + 1
        self.maxFreq = max(self.maxFreq, self.freqMap[val])
        self.stackList[self.freqMap[val]].append(val)
        
    def pop(self) -> int:
        while self.maxFreq > 0 and len(self.stackList[self.maxFreq]) == 0:
            self.maxFreq -= 1
        # print(self.maxFreq)
        val = self.stackList[self.maxFreq].pop()
        self.freqMap[val] -= 1
        return val

        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()