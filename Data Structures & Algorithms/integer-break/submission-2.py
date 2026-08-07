class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [0 for i in range(n + 1)]
        memo[0] = 1
        for curr in range(1, n + 1):
            for i in range(1, n):
                if curr - i < 0:
                    break
                memo[curr] = max(memo[curr - i] * i, memo[curr])
        return memo[-1]


        # memo = {}
        # def util(curr):
        #     if curr == 0:
        #         return 1
        #     if curr in memo:
        #         return memo[curr]
        #     v = 1
        #     for i in range(1, n):
        #         if curr - i < 0:
        #             break
        #         v = max(v, util(curr - i) * i)
        #     memo[curr] = v
        #     return v
        # return util(n)
