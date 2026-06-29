class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def util(i, j, k):
            if i >= len(s1) and j >= len(s2):
                return True
            if i >= len(s1):
                if s2[j:] == s3[k]:
                    return True
                return False
            if j >= len(s2):
                if s1[i:] == s3[k:]:
                    return True
                return False
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            if s1[i] == s3[k]:
                if util(i+1, j, k+1):
                    memo[(i, j, k)] = True
                    return memo[(i, j, k)]
        
            if s2[j] == s3[k]:
                if util(i, j+1, k+1):
                    memo[(i, j, k)] = True
                    return memo[(i, j, k)]
        
            memo[(i, j, k)] = False
            return memo[(i, j, k)]
        return util(0,0,0)
            
            


