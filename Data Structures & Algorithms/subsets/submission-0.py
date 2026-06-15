class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        def util(index):
            if index >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[index])
            util(index+1)
            curr.pop()
            util(index+1)
        util(0)
        return res

            

            