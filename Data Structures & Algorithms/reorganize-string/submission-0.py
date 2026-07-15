class Solution:
    def reorganizeString(self, s: str) -> str:
        waitingQ = collections.deque()
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
            if count != 0:
                waitingQ.append((count, ele))
            while waitingQ and waitingQ[0][1] != ele:
                heapq.heappush(heap, waitingQ.popleft())

        if waitingQ:
            return ''
        return ''.join(res)
        
            
            
            
            

