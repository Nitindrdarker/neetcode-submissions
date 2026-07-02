class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def util(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            res = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += util(l, i - 1) + util(i+1, r)
                res = max(res, coins)
            memo[(l, r)] = res
            return res
        return util(1, len(nums) - 2)
            