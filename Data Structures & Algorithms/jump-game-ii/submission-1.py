class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [len(nums) + 1 for i in range(len(nums) + 1)]
        for index in range(len(nums), -1, -1):
            if index >= len(nums) - 1:
                memo[index] = 0
                continue
            v = len(nums) - 1
            for i in range(index, index+nums[index]):
                if i + 1 <= len(nums):
                    v = min(v, memo[i+1] + 1)
            memo[index] = v
        return memo[0]



    #     # memo = {}
    #     # def util(index):
    #     #     if index >= len(nums) - 1:
    #     #         return 0
    #     #     if index in memo:
    #     #         return memo[index]
    #     #     v = len(nums) - 1
            
    #     #     for i in range(index, index + nums[index]):
    #     #         v = min(util(i+1) + 1, v)
    #     #     memo[index] = v
    #     #     return v
    #     # return util(0)
            

