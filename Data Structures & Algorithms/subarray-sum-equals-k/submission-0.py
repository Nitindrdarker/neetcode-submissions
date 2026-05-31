class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0:1}
        s = 0
        res = 0
        for i in nums:
            s += i
            if s - k in m:
                res += m[s - k]
            m[s] = m.get(s, 0) + 1
            # print(m, res)
        return res
