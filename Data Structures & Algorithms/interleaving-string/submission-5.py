class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        memo[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i >= len(s1) and j >= len(s2):
                    memo[i][j] = True
                    continue
                if i >= len(s1):
                    if s2[j:] == s3[i+j:]:
                        memo[i][j] = True
                        continue
                if j >= len(s2):
                    if s1[i:] == s3[i+j:]:
                        memo[i][j] = True
                        continue
                if i < len(s1) and j < len(s2) and s1[i] == s3[i+j]:
                    if memo[i+1][j]:
                        memo[i][j] = True
                if i < len(s1) and j < len(s2) and s2[j] == s3[i+j]:
                    if memo[i][j+1]:
                        memo[i][j] = True
        return memo[0][0]
                        
                
                    



        # memo = {}
        # def util(i, j):
        #     if i >= len(s1) and j >= len(s2):
        #         return True
        #     if i >= len(s1):
        #         if s2[j:] == s3[i+j:]:
        #             return True
        #         return False
        #     if j >= len(s2):
        #         if s1[i:] == s3[i+j:]:
        #             return True
        #         return False
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if s1[i] == s3[i+j]:
        #         if util(i+1, j):
        #             memo[(i, j)] = True
        #             return memo[(i, j)]
        
        #     if s2[j] == s3[i+j]:
        #         if util(i, j+1):
        #             memo[(i, j)] = True
        #             return memo[(i, j)]
        
        #     memo[(i, j)] = False
        #     return memo[(i, j)]
        # return util(0,0)
            
            


