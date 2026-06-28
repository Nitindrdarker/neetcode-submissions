class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)
        if abs(target) > offset:
            return 0

        

        memo = [[0] * (2 * offset + 1) for _ in range(len(nums) + 1)]
        memo[len(nums)][target + offset] = 1

        for index in range(len(nums) - 1, -1, -1):
            for curr in range(-offset, offset+1, 1):
                add = sub = 0
                if curr + nums[index] <= offset:
                    add = memo[index+1][curr + nums[index] + offset]
                if curr - nums[index] >= -offset:
                    sub = memo[index+1][curr - nums[index] + offset]
                memo[index][curr + offset] = add + sub
        return memo[0][offset]

        # def dfs(index, curr):
        #     if index == len(nums):
        #         return 1 if curr == target else 0

        #     if memo[index][curr + offset] != -1:
        #         return memo[index][curr + offset]

        #     add = dfs(index + 1, curr + nums[index])
        #     sub = dfs(index + 1, curr - nums[index])

        #     memo[index][curr + offset] = add + sub
        #     return memo[index][curr + offset]

        # return dfs(0, 0)