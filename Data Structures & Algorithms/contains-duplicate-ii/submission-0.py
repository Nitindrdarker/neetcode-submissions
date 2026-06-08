class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i, val in enumerate(nums):
            if val in h:
                if i - h[val] <= k:
                    return True

            h[val] = i
        return False