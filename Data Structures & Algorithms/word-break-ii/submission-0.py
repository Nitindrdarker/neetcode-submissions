class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictSet = set(wordDict)
        curr = []
        res = []
        def util(index):
            
            if index >= len(s):
                res.append(' '.join(curr))
                return 
            for i in range(index, len(s)):
                subStr = s[index:i+1]
                if subStr in dictSet:
                    curr.append(subStr)
                    util(i+1)
                    curr.pop()
        util(0)
        return res