class Solution:
    def reorganizeString(self, s: str) -> str:
        waitingQ = ()
        q = [-1, -1]
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        heap = []
        res = []
        for i in freq:
            heapq.heappush(heap, (-1 * freq[i], i))
        while heap:
            count, ele = heapq.heappop(heap)
            res.append(ele)
            count = count + 1
            if waitingQ and waitingQ[1] != ele:
                heapq.heappush(heap, waitingQ)
                waitingQ = ()
            if count != 0:
                waitingQ = (count, ele)
        if waitingQ:
            return ''
        return ''.join(res)
        
            
            
            
            

