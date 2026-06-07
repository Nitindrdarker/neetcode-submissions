class HeapQ:
    def __init__(self, l):
        self.heap = l
        for i in range(len(l) // 2, -1, -1):
            self.heapify(i)


    def heapify(self, index):
        minimum = index
        left = index * 2 + 1
        right = index * 2 + 2
        
        if left < len(self.heap) and self.heap[minimum] > self.heap[left]:
            minimum = left
        if right < len(self.heap) and self.heap[minimum] > self.heap[right]:
            minimum = right
        if minimum != index:
            self.heap[minimum], self.heap[index] = self.heap[index], self.heap[minimum]
            self.heapify(minimum)

    def pop(self):
        
        lastEle = self.heap.pop()
        if len(self.heap) == 0:
            return lastEle
        top = self.heap[0]
        self.heap[0] = lastEle
        self.heapify(0)
        return top





class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heap = HeapQ(nums)
        while len(heap.heap) > 0:
            res.append(heap.pop())
        return res

        