class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = [0, 1, 1, 2]
        if n <= 3:
            return memo[n]
        n -= 3
        while n > 0:
            c = memo[3]
            memo[3] = memo[3] + memo[2] + memo[1]
            memo[0] = memo[1]
            memo[1] = memo[2]
            memo[2] = c
            n -= 1
            # print(memo)
        return memo[-1]
            