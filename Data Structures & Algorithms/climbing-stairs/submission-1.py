class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [0 for i in range(n+2)]
        memo[n] = 1
        for step in range(n-1, -1, -1):
            one = memo[step + 1]
            two = memo[step + 2]
            memo[step] = one + two
        return memo[0]

        
            
