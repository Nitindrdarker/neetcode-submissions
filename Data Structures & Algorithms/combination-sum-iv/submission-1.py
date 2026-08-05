class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = [0 for i in range(target + 1)]
        memo[target] = 1
        for curr in range(target-1, -1, -1):
            v = 0
            for i in range(len(nums)):
                if curr + nums[i] <= target:
                    v += memo[curr + nums[i]]
            memo[curr] = v
        return memo[0]