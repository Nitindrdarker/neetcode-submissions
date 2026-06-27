class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def util(index, curr):
            if curr == amount:
                return 1

            if curr > amount:
                return 0
            if index >= len(coins):
                return 
            if (index, curr) in memo:
                return memo[(index, curr)]
            v = 0
            for i in range(index, len(coins)):
                v += util(i, curr + coins[i])
            memo[(index, curr)] = v
            return memo[(index, curr)]
        return util(0, 0)
            