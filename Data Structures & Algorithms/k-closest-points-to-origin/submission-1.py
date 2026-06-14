class Solution:
    def calcDist(self,x2, y2):
        x1 = y1 = 0
        return (x1 - x2) ** 2 + (y1 - y2) ** 2
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x2, y2 in points:
            dist = self.calcDist(x2, y2)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-1 * dist, (x2, y2)))
            else:
                if -1 * maxHeap[0][0] > dist:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-1 * dist, (x2, y2)))
        res = []
        print(maxHeap)
        for i in maxHeap:
            res.append(i[1])
        return res


        