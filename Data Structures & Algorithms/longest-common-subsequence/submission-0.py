class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = len(text1)
        b = len(text2)
        memo = [[0 for i in range(b+1)] for j in range(a+1)]

        def util(i, j):
            if i >= a or j >= b or i < 0 or j < 0:
                return 0
            if memo[i][j] != 0:
                return memo[i][j]
            match = skip1 = skip2 = 0

            if text1[i] == text2[j]:
                match = util(i + 1, j + 1) + 1
            skip1 = util(i + 1, j)
            skip2 = util(i, j + 1)
            memo[i][j] = max(skip1, skip2, match)
            return memo[i][j]
        return util(0, 0)
            
                 
