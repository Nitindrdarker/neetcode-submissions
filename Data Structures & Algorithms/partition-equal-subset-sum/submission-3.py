class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        memo = [False for i in range(total + 1)]

        for index in range(len(nums)-1, -1, -1):
            temp = [False for i in range(total + 1)]
            for currSum in range(target, -1, -1):
                if currSum == target:
                    memo[currSum] = True
                    continue
                if currSum > target:
                    memo[currSum] = False
                    continue
                if index >= len(nums):
                    memo[currSum] = False
                    continue
                skip = memo[currSum]
                take = memo[currSum + nums[index]]
                temp[currSum] = skip or take
            memo = temp.copy()
                
        return memo[0]
            