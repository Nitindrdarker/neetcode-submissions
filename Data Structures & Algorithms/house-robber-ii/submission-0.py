class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.rob2(nums[:-1]), self.rob2(nums[1:]))

    def rob2(self, nums: List[int]) -> int:
        memo = [0 for i in range(len(nums) + 2)]
        memo[len(nums)] = 0
        def util(index):
            if index >= len(nums):
                return 0
            if memo[index] != 0:
                return memo[index]
            take = nums[index] + util(index + 2)
            skip = util(index+1)
            memo[index] = max(take, skip)
            return memo[index]
        return util(0)
    
        
