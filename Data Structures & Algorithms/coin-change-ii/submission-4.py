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
                take = memo[index][curr + coins[index]] if curr + coins[index] <= amount else 0
                skip = memo[index+1][curr]
                
                
                memo[index][curr] = take + skip
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
            
        #     take = util(index, curr + coins[index])
        #     skip = util(index+1, curr)
        #     memo[(index, curr)] = take + skip
        #     return memo[(index, curr)]
        # return util(0, 0)
            