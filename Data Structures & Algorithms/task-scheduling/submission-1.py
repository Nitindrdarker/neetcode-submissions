class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for i in tasks:
            freqMap[i] = freqMap.get(i, 0) + 1


        maxHeap = []
        q = collections.deque()
        for i in freqMap:
            heapq.heappush(maxHeap, (-1 * freqMap[i], 0, i))

        t = 0
        while maxHeap or q:
            
            while q and q[0][1] <= t:
                f, time, task = q.popleft()
                heapq.heappush(maxHeap, (-1 * f, time, task))
            
            if maxHeap:
                f, time, task = heapq.heappop(maxHeap)
                f = -1 * f
                f -= 1
                t += 1
                if f > 0:
                    q.append((f, n + t, task))
            else:
                t = q[0][1]
            
        return t
            


        




            

        
        


            
        