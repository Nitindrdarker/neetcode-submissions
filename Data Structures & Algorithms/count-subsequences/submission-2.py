class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

        for i in range(len(s), -1, -1):
            for j in range(len(t), -1, -1):
                if j >= len(t):
                    memo[i][j] = 1
                    continue
                if i >= len(s) or j >= len(t):
                    continue
                a = b = 0
                if s[i] == t[j]:
                    a = memo[i+1][j+1]
                b = memo[i+1][j]
                memo[i][j] = a + b
        return memo[0][0]







        # memo = {}
        # def util(i, j):
        #     if j >= len(t):
        #         return 1
        #     if i >= len(s) or j >= len(t):
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     a = b = 0
        #     if s[i] == t[j]:
        #         a = util(i+1, j+1)
        #     b = util(i+1, j)
        #     memo[(i, j)] = a + b
        #     return memo[(i, j)]
        # return util(0, 0)

           
