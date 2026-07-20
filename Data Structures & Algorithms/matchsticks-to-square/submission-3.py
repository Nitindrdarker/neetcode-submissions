class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLength = sum(matchsticks)
        if totalLength % 4:
            return False
        sideLength = totalLength // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > sideLength:
            return False
        def util(idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                if sides[i] + matchsticks[idx] <= sideLength:
                    sides[i] += matchsticks[idx]
                    if util(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
                if sides[i] == 0:
                    return False
            return False
        return util(0)


                    

        
