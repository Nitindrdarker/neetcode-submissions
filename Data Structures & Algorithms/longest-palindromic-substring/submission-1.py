class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1, -1]
        for i in range(len(s)):
            a = self.findLongest(i, i, s)
            b = self.findLongest(i, i+1, s)
            if a[1] - a[0] > res[1] - res[0]:
                res = a
            if b[1] - b[0] > res[1] - res[0]:
                res = b
        return s[res[0]:res[1]]

    def findLongest(self, i, j, s):
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1 
            else:
                break
        return [i+1, j]
    