class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            s += nums[right]
            while left <= right and s >= target:
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1
        return res if res != len(nums) + 1 else 0

