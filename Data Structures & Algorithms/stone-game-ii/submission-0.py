class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def util(alice, index, window):
            if index >= len(piles):
                return 0
            if (alice, index, window) in memo:
                return memo[(alice, index, window)]
            total = 0
            res = 0
            if not alice:
                res = float("inf")
            for i in range(1, 2 * window + 1):
                if index + i > len(piles):
                    break
                total += piles[i + index - 1]
                if alice:
                    res = max(res, total + util(False, index + i, max(window, i)))
                else:
                    res = min(res, util(True, index + i, max(window, i)))
                
            memo[(alice, index, window)] = res
            return memo[(alice, index, window)]
        return util(True, 0, 1)
            
