class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        def solve(i, groupA, groupB):
            if i == len(stones):
                return abs(groupA - groupB)
            if (i, groupA, groupB) in memo:
                return memo[(i, groupA, groupB)]
            # Put current stone in group A
            option1 = solve(
                i + 1,
                groupA + stones[i],
                groupB
            )

            # Put current stone in group B
            option2 = solve(
                i + 1,
                groupA,
                groupB + stones[i]
            )

            memo[(i, groupA, groupB)] = min(option1, option2)
            return memo[(i, groupA, groupB)]

        return solve(0, 0, 0)
                
            
            
            