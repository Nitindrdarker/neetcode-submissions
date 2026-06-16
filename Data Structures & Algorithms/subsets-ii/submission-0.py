class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        nums.sort()
        def util(index):
            res.append(curr.copy())
            if index >= len(nums):
                return 
            for i in range(index, len(nums)):
                if i > index and nums[i-1] == nums[i]:
                    continue
                curr.append(nums[i])
                util(i + 1)
                curr.pop()
        util(0)
        return res