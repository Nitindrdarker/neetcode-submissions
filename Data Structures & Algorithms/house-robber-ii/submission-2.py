class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob2(nums[:-1]), self.rob2(nums[1:]))

    def rob2(self, nums: List[int]) -> int:
        prev = 0
        prevprev = 0
        for index in range(len(nums) - 1, -1, -1):
            take = nums[index] + prevprev
            skip = prev
            prevprev = prev
            prev = max(take, skip)
        return prev
    
        
