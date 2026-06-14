class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        while True:
            pivot = nums[right]
            idx = left

            for i in range(left, right):
                if nums[i] >= pivot:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    idx += 1

            nums[idx], nums[right] = nums[right], nums[idx]

            if idx + 1 == k:
                return nums[idx]
            elif idx + 1 < k:
                left = idx + 1
            else:
                right = idx - 1