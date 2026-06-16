class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        visited = set()
        def util():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                curr.append(nums[i])
                visited.add(i)
                util()
                curr.pop()
                visited.remove(i)
        util()
        return res
            
            