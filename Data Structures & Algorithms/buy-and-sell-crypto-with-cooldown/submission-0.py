class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def util(index, isBuyed):
            if index >= len(prices):
                return 0
            if (index, isBuyed) in memo:
                return memo[(index, isBuyed)]
            a = b = skip = 0
            if isBuyed:
                a = util(index + 2, False) + prices[index]
            else:
                b = util(index + 1, True) - prices[index]
            skip = util(index+1, isBuyed)
            memo[(index, isBuyed)] = max(a, b, skip)
            return memo[(index, isBuyed)]
        return util(0, False)