class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = []
        for i in range(len(intervals)):
            
            if res and (res[-1][1] > intervals[i][0] and res[-1][0] < intervals[i][1]):
                continue
            else:
                res.append(intervals[i])
        return len(intervals) - len(res)