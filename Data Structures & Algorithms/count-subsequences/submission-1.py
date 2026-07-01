class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def util(i, j):
            if j >= len(t):
                return 1
            if i >= len(s) or j >= len(t):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
                
            a = b = 0
            if s[i] == t[j]:
                a = util(i+1, j+1)
            b = util(i+1, j)
            
            memo[(i, j)] = a + b
            return memo[(i, j)]
        return util(0, 0)

           
