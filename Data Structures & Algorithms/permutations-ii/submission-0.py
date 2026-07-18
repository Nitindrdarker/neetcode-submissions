class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = {}
        res = []
        curr = []
        for i in nums:
            visited[i] = visited.get(i, 0) + 1
        def util():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in visited:
                if visited[i] > 0:
                    curr.append(i)
                    visited[i] -= 1
                    util()
                    visited[i] += 1
                    curr.pop()
        util()
        return res




            

            

