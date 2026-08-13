class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        _max = float("-inf")
        _min = float("inf")

        currMax = 0
        currMin = 0
        s = 0

        for x in nums:
            currMax = max(currMax + x, x)
            _max = max(_max, currMax)

            currMin = min(currMin + x, x)
            _min = min(_min, currMin)

            s += x

        if _max < 0:
            return _max

        return max(_max, s - _min)