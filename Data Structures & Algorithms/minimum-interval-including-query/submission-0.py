class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQ = sorted([v, i] for i, v in enumerate(queries))
        i = 0
        minHeap = []
        res = [-1 for i in range(len(queries))]
        for val, idx in sortedQ:
            while i < len(intervals) and intervals[i][0] <= val:
                left, right = intervals[i]
                heapq.heappush(minHeap, (right - left + 1, right))
                i += 1
            
            while minHeap and minHeap[0][1] < val:
                heapq.heappop(minHeap)
            
            if minHeap:
                res[idx] = minHeap[0][0]
        return res


