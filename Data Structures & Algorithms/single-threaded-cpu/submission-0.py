class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pairs = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        heapq.heapify(pairs)
        t = 0
        q = []
        res = []
        while pairs or q:
            if len(q) == 0:
                t = pairs[0][0]
                while pairs and pairs[0][0] <= t:
                    et, pt, idx = heapq.heappop(pairs)
                    heapq.heappush(q, (pt, idx))
            else:
                pt, idx = heapq.heappop(q)
                t += pt
                res.append(idx)
                while pairs and pairs[0][0] <= t:
                    et, pt, idx = heapq.heappop(pairs)
                    heapq.heappush(q, (pt, idx))
        
        return res





                

        


