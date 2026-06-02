class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            res = max(currMax, res)
        return res
