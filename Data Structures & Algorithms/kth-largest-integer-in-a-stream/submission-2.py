class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] # min heap
        for i in nums:
            self.add(i)
        
        

    def add(self, val: int) -> int:
        
        if len(self.heap) >= self.k:
            if self.heap[0] < val:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
                return self.heap[0]
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
            
        
