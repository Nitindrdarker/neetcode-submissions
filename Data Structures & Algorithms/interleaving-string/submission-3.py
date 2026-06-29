class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def util(i, j):
            if i >= len(s1) and j >= len(s2):
                return True
            if i >= len(s1):
                if s2[j:] == s3[i+j]:
                    return True
                return False
            if j >= len(s2):
                if s1[i:] == s3[i+j:]:
                    return True
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            if s1[i] == s3[i+j]:
                if util(i+1, j):
                    memo[(i, j)] = True
                    return memo[(i, j)]
        
            if s2[j] == s3[i+j]:
                if util(i, j+1):
                    memo[(i, j)] = True
                    return memo[(i, j)]
        
            memo[(i, j)] = False
            return memo[(i, j)]
        return util(0,0)
            
            


