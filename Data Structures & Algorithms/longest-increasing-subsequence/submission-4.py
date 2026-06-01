class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def util(index):
            if index in memo:
                return memo[index]
            c = 0
            for i in range(index, len(nums)):
                if nums[index] < nums[i]:
                    c = max(c, util(i) + 1)
            memo[index] = c
            return memo[index]
        v = 0
        for idx in range(len(nums)):
            v = max(v,util(idx) + 1)
        return v


            
