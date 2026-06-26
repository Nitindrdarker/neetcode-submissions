class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[0 for i in range(2)] for j in range(len(prices) + 2)]
        for index in range(len(prices) - 1, -1, -1):
            # 0 - False, 1 - True
            for isBuyed in range(1, -1, -1):
                a = b = skip = 0
                if isBuyed:
                    a = memo[index+2][0] + prices[index]
                else:
                    b = memo[index+1][1] - prices[index]
                skip = memo[index+1][isBuyed]
                memo[index][isBuyed] = max(a, b, skip)
        return memo[0][0]



        # memo = {}
        # def util(index, isBuyed):
        #     if index >= len(prices):
        #         return 0
        #     if (index, isBuyed) in memo:
        #         return memo[(index, isBuyed)]
        #     a = b = skip = 0
        #     if isBuyed:
        #         a = util(index + 2, False) + prices[index]
        #     else:
        #         b = util(index + 1, True) - prices[index]
        #     skip = util(index+1, isBuyed)
        #     memo[(index, isBuyed)] = max(a, b, skip)
        #     return memo[(index, isBuyed)]
        # return util(0, False)