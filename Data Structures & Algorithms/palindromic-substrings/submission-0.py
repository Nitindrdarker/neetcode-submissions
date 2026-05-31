class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.findLongest(i, i+1, s) + self.findLongest(i, i, s)
        return res

    

    def findLongest(self, i, j, s):
        count = 0
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1 
                count += 1
            else:
                break
        return count
    