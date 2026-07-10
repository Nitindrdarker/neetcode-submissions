class Solution:
    def jump(self, nums: List[int]) -> int:
        lastReached = 0
        r = l = 0
        res = 0
        while r < len(nums) - 1:
            lastReached = 0
            for i in range(l, r + 1):
                lastReached = max(lastReached, i + nums[i])
            l = r + 1
            r = lastReached
            res += 1
        return res

