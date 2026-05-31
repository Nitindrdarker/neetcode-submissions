class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(n+1)]
        def util(step):
            if step == n:
                return 1
            if step > n:
                return 0
            if memo[step] != 0:
                return memo[step]
            one = util(step + 1)
            two = util(step + 2)
            memo[step] = one + two
            return memo[step]
        return util(0)
            
