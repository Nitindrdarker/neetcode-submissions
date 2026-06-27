class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]

        for index in range(len(coins) - 1, -1, -1):
            for curr in range(amount, -1, -1):
                if curr == amount:
                    memo[index][curr] = 1
                    continue
                if curr > amount:
                    continue
                v = 0
                
                for i in range(index, len(coins)):
                    
                    temp = memo[i][curr + coins[i]] if curr + coins[i] <= amount else 0
                    
                    v += temp
                memo[index][curr] = v
        return memo[0][0]
                






        # memo = {}
        # def util(index, curr):
        #     if curr == amount:
        #         return 1
        #     if curr > amount:
        #         return 0
        #     if index >= len(coins):
        #         return 0
        #     if (index, curr) in memo:
        #         return memo[(index, curr)]
        #     v = 0
        #     for i in range(index, len(coins)):
        #         v += util(i, curr + coins[i])
        #     memo[(index, curr)] = v
        #     return memo[(index, curr)]
        # return util(0, 0)
            