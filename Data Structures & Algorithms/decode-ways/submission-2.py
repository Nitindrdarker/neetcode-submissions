class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None for i in range(len(s) + 2)]
        memo[len(s)] = 1

        def util(index):
            if index == len(s):
                return 1
            if index > len(s):
                return 0
            if s[index] == '0':
                return 0
            
            if memo[index] != None:
                return memo[index]
            a = b = 0
            a = util(index+1)
            if s[index:index+2] <= "26":
                b = util(index+2)
            memo[index] = a + b
            return a + b
        return util(0)

                
