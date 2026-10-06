class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        for i in range(1, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]

        

        