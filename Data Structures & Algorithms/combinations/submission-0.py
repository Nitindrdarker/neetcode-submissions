class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        res = []
        def util(num):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if num > n:
                return 
            curr.append(num)
            util(num + 1)
            curr.pop()
            util(num + 1)
        util(1)
        return res
