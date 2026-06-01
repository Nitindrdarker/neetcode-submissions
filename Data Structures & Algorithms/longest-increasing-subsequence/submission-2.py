class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo = [[None for i in range(max(nums) + 1)] for j in range(len(nums) + 1)]
        memo = {}
        def util(index, prev):
            if index >= len(nums):
                return 0
            if (index, prev) in memo:
                return memo[(index, prev)]
            if nums[index] <= prev:
                return util(index + 1, prev)
            take = skip = 0
            take = util(index + 1, nums[index]) + 1
            skip = util(index + 1, prev)
            memo[(index, prev)] = max(take, skip)
            return memo[(index, prev)]
        return util(0, -float("inf"))


            
