class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        freq = {'': 0}
        res = ''
        for word in strs:
            pref = ''
            for c in word:
                pref += c
                freq[pref] = freq.get(pref, 0) + 1
                if len(res) < len(pref) and freq[pref] == len(strs):
                    res = pref
        return res
        
