class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        start = 0
        end = len(nums) - 1
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            start = pivot
        else:
            end = pivot - 1

        
        print(start, end)
        while start <= end:
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            while start < end and nums[end] == nums[end - 1]:
                end -= 1
            mid = (start + end) // 2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False

            

            