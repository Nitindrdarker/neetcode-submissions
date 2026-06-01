class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictSet = set(wordDict)
        memo = [False for i in range(len(s) + 1)]
        memo[len(s)] = True

        for index in range(len(s) - 1, -1, -1):
            for i in range(index, len(s)):
                subString = s[index:i+1]
                if subString in dictSet:
                    if memo[i + 1] == True:
                        memo[index] = True
                        break
            if memo[index] != True:
                memo[index] = False
        return memo[0]

        # def util(index):
        #     if len(s) <= index:
        #         return True
        #     if memo[index] != None:
        #         return memo[index]
        #     for i in range(index, len(s)):
        #         subString = s[index: i+1]
        #         if subString in dictSet:
        #             if util(i+1) == True:
        #                 memo[index] = True
        #                 return True
        #     memo[index] = False
        #     return False
        # return util(0)
            

