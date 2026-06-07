class HeapQ:
    def __init__(self, l):
        self.heap = l
        for i in range(len(l) // 2, -1, -1):
            self.heapify(i)


    def heapify(self, index):
        n = len(self.heap)

        while True:
            minimum = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[minimum]:
                minimum = left

            if right < n and self.heap[right] < self.heap[minimum]:
                minimum = right

            if minimum == index:
                break

            self.heap[index], self.heap[minimum] = (
                self.heap[minimum],
                self.heap[index]
            )

            index = minimum

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

        