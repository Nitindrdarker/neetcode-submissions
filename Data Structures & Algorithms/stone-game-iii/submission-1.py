class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = [0 for i in range(len(stoneValue) + 1)]
        memo[-1] = 0
        for index in range(len(stoneValue) - 1, -1, -1):
            v = 0
            diff = float("-inf")
            for i in range(3):
                if index + i >= len(stoneValue):
                    break
                v += stoneValue[index + i]
                diff = max(diff, v - memo[index + i + 1])
            memo[index] = diff
        d = memo[0]
        if d > 0:
            return "Alice"
        elif d < 0:
            return "Bob"
        else:
            return "Tie"



        # memo = {}
        # def util(index):
        #     if index >= len(stoneValue):
        #         return 0
        #     if index in memo:
        #         return memo[index]
        #     v = 0
        #     diff = float("-inf")
        #     for i in range(3):
        #         if index + i >= len(stoneValue):
        #             break
        #         v += stoneValue[index + i]
        #         diff = max(diff, v - util(index + i + 1))
        #     memo[index] = diff
        #     return diff
        # d = util(0)
        # if d > 0:
        #     return "Alice"
        # elif d < 0:
        #     return "Bob"
        # else:
        #     return "Tie"




