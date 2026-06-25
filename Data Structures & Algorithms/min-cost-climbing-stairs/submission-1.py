class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = [0 for i in range(len(cost) + 2)]
        for index in range(len(cost) - 1, -1, -1):
            one = memo[index+1] + cost[index]
            two = memo[index+2] + cost[index]
            memo[index] = min(one, two)
        return min(memo[0], memo[1])



        # memo = {}
        # def util(index):
        #     if index >= len(cost):
        #         return 0
        #     if index in memo:
        #         return memo[index]
        #     one = util(index+1) + cost[index]
        #     two = util(index+2) + cost[index]
        #     memo[index] = min(one, two)
        #     return memo[index]
        # return min(util(0), util(1))