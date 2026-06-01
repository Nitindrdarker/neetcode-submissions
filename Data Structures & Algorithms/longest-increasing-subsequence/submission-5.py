class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0 for i in range(len(nums) + 1)]
        def util(index):
            if memo[index] != 0:
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


            
