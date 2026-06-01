class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum = nums[0]
        maximum = nums[0]
        res = -float("inf")
        for i in range(1, len(nums)):
            temp = maximum
            maximum = max(maximum * nums[i], nums[i], minimum * nums[i])
            minimum = min(minimum * nums[i], nums[i], temp * nums[i])
            res = max(res, maximum)
        return max(maximum, res)
