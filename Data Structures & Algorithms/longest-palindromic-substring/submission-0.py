class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            a = self.findLongest(i, i, s)
            b = self.findLongest(i, i+1, s)
            if len(a) > len(res):
                res = a
            if len(b) > len(res):
                res = b
        return res

    def findLongest(self, i, j, s):
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1 
            else:
                break
        return s[i+1: j]
    