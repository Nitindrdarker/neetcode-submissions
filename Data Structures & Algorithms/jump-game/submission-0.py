class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastTrue = len(nums) - 1
        for i in range(len(nums) - 2, -1 ,-1):
           
            if lastTrue - i <= nums[i]:
                lastTrue = i
            
        return lastTrue == 0
