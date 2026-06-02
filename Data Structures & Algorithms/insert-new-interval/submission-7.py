class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                for j in range(i + 1, len(intervals)):
                    if newInterval[1] < intervals[j][0]:
                        return res + [newInterval] + intervals[j:]
                    else:
                        newInterval[1] = max(intervals[j][1], newInterval[1])
                return res + [newInterval]
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                res.append(intervals[i])
        if newInterval not in res:
            res.append(newInterval)
        return res