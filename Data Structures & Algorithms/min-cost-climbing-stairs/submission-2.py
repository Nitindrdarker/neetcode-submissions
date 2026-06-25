class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        next = 0
        nextNext = 0
    
        for index in range(len(cost) - 1, -1, -1):
            one = next + cost[index]
            two = nextNext + cost[index]
            nextNext = next

            next = min(one, two)
        return min(next, nextNext)



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