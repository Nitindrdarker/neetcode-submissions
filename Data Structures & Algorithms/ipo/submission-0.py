class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pair = [(capital[i], profits[i]) for i in range(len(profits))]
        # print(pair)
        res = []
        heapq.heapify(pair)
        maxProfHeap = [] # with only k length
        count = 0
        while pair:
            cap, prof = heapq.heappop(pair)
            
            if cap <= w:
                heapq.heappush(maxProfHeap, (-1 * prof, cap))
                
            else:
                if maxProfHeap and count < k:
                    pro, ca = heapq.heappop(maxProfHeap)
                    w += (-1 * pro)
                    count += 1
                if count >= k:
                    break
                if cap <= w:
                    heapq.heappush(maxProfHeap, (-1 * prof, cap))
        while maxProfHeap and count < k:
                pro, ca = heapq.heappop(maxProfHeap)
                w += (-1 * pro)
                count += 1
        return w
        
            
                

                

            



            
            

            


            



