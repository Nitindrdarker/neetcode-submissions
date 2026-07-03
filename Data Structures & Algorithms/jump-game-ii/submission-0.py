class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def util(index):
            if index >= len(nums) - 1:
                return 0
            if index in memo:
                return memo[index]
            v = len(nums) - 1
            
            for i in range(index, index + nums[index]):
                v = min(util(i+1) + 1, v)
            memo[index] = v
            return v
        return util(0)
            

