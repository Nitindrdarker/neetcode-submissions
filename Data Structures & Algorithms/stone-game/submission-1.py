class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def util(s, e):
            if s > e:
                return 0
            if (s, e) in memo:
                return memo[(s, e)]
            c1 = c2 = 0
            c1 += piles[s]
            diff1 = c1 - util(s+1, e)
            

            c2 += piles[e]
            diff2 = c2 - util(s, e-1)
            
            memo[(s, e)] = max(diff1, diff2)
            return memo[(s, e)]
        d = util(0, len(piles) - 1)
        return d > 0

            