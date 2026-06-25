class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        memo = [[False for i in range(total + 1)] for i in range(len(nums) + 1)]

        for index in range(len(nums)-1, -1, -1):
            for currSum in range(target, -1, -1):
                if currSum == target:
                    memo[index][currSum] = True
                    continue
                if currSum > target:
                    memo[index][currSum] = False
                    continue
                if index >= len(nums):
                    memo[index][currSum] = False
                    continue
                skip = memo[index+1][currSum]
                take = memo[index+1][currSum + nums[index]]
                memo[index][currSum] = skip or take
                
        return memo[0][0]
            