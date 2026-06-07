class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = m


        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if index >= len(nums):
                continue
            nums[index] = -1 * abs(nums[index])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return m

            
