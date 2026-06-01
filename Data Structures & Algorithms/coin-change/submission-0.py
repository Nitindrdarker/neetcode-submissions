class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [None for i in range(amount+1)]
        def util(curr):
            print(curr)
            if curr == amount:
                return 0
            if curr > amount:
                return float("inf")
            if dp[curr] != None:
                return dp[curr]
            v = float("inf")
            for index in range(len(coins)):
                v = min(util(curr + coins[index]) + 1, v)
            dp[curr] = v
            return dp[curr]
        
        res = util(0)
        return res if res != float("inf") else -1

