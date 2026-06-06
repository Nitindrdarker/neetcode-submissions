class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorEle = 0
        for i in range(len(nums)):
            if count == 0:
                count += 1
                majorEle = nums[i]
            elif majorEle == nums[i]:
                count += 1
            else:
                count -= 1
        return majorEle
            
                
