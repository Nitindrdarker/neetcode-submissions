class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select
        def pivot(left, right):
            while True:
                if left >= right:
                    return nums[left]
                p = right
                idx = left
                for i in range(left, right):
                    if nums[i] >= nums[p]:
                        nums[idx], nums[i] = nums[i], nums[idx]
                        idx += 1
                nums[idx], nums[p] = nums[p], nums[idx]
                if idx + 1 == k:
                    return nums[idx]
                elif idx + 1 < k:
                    left = idx + 1

                else:
                    right = idx - 1
        return pivot(0, len(nums) - 1)
        





        


