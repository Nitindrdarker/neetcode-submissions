class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def util(index):
            if index >= len(s):
                res.append(curr.copy())
                return
            for i in range(index, len(s)):
                sub = s[index:i+1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    util(i+1)
                    curr.pop()
        util(0)
        return res
            
