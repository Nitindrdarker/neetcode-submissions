class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def util(curr):
            if curr == 0:
                return 1
            if curr in memo:
                return memo[curr]
            v = 1
            for i in range(1, n):
                if curr - i < 0:
                    break
                v = max(v, util(curr - i) * i)
            memo[curr] = v
            return v
        return util(n)
