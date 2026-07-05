class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, v in enumerate(s):
            lastIndex[v] = i
        res = []
        maxIndex = -1
        last = -1
        
        for i in range(len(s)):
            c = s[i]
            maxIndex = max(lastIndex[c], maxIndex)
            if i == maxIndex:
                res.append(i - last)
                last = i
        return res



        

        
            

            
            

        
        
        