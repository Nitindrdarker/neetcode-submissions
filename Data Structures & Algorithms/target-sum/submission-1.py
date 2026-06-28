class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def util(index, curr):
            
            
            if index >= len(nums):
                if curr == target:
                    return 1
                return 0
            if (index, curr) in memo:
                return memo[(index, curr)]
            add = util(index+1, curr + nums[index])
            sub = util(index+1, curr - nums[index])
            memo[(index, curr)] = add + sub
            return memo[(index, curr)]
        return util(0, 0)
