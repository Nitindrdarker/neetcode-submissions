class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pair = [(capital[i], profits[i]) for i in range(len(profits))]
        # print(pair)
        res = []
        heapq.heapify(pair)
        maxProfHeap = [] # with only k length
        count = 0
        while pair:
            
            
            while pair and pair[0][0] <= w:
                cap, prof = heapq.heappop(pair)
                heapq.heappush(maxProfHeap, (-1 * prof, cap))
                
            
            if maxProfHeap and count < k:
                pro, ca = heapq.heappop(maxProfHeap)
                w += (-1 * pro)
                count += 1
            else:
                break
                
        while maxProfHeap and count < k:
                pro, ca = heapq.heappop(maxProfHeap)
                w += (-1 * pro)
                count += 1
        return w