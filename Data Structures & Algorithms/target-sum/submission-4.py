class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)

        # If target is outside the possible range, no solution exists.
        # if abs(target) > offset:
        #     return 0

        memo = [[-1] * (2 * offset + 1) for _ in range(len(nums) + 1)]

        def dfs(index, curr):
            if index == len(nums):
                return 1 if curr == target else 0

            if memo[index][curr + offset] != -1:
                return memo[index][curr + offset]

            add = dfs(index + 1, curr + nums[index])
            sub = dfs(index + 1, curr - nums[index])

            memo[index][curr + offset] = add + sub
            return memo[index][curr + offset]

        return dfs(0, 0)