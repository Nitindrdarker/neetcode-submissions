class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        waitingQ = collections.deque()
        heap = []
        res = []
        if a:
            heapq.heappush(heap, (-1*a, 'a'))
        if b:
            heapq.heappush(heap, (-1*b, 'b'))
        if c:
            heapq.heappush(heap, (-1*c, 'c'))
        
        while heap:
            count, ele = heapq.heappop(heap)
            count += 1
            res.append(ele)
            if waitingQ:
                heapq.heappush(heap, (waitingQ.popleft()))
            if count != 0:
                if len(res) < 2 or res[-2] != ele:
                    heapq.heappush(heap, (count, ele))
                else:
                    waitingQ.append((count, ele))
        return ''.join(res)
            





        
            
            
            
            


        
            
            
            
            


