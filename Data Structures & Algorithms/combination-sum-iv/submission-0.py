class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def util(curr):
            if curr == target:
                return 1
            if curr > target:
                return 0
            if curr in memo:
                return memo[curr]
            v = 0
            for i in range(len(nums)):
                v += util(curr + nums[i])
            memo[curr] = v
            return v
        return util(0)

