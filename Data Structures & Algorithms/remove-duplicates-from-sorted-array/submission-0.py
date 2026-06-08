class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        i = 0
        while i < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            nums[left] = nums[i]
            i += 1
            left += 1
        return left
            


