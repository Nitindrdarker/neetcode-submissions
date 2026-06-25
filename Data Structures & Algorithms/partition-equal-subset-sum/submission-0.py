class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        memo = {}
        def util(index, currSum):
            if currSum == target:
                return True
            if currSum > target:
                return False
            if index >= len(nums):
                return False
            if (index, currSum) in memo:
                return memo[(index, currSum)]
            skip = util(index+1, currSum)
            take = util(index+1, currSum + nums[index])
            memo[(index, currSum)] = skip or take
            return memo[(index, currSum)]
        return util(0, 0)
            