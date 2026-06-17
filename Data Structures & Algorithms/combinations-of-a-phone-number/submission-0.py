class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        curr = []
        def util(index):
            if index >= len(digits):
                if len(curr) > 0 and len(curr) == len(digits):
                    res.append(''.join(curr))
                return 
            digit = digits[index]
            if digit not in charMap:
                return 
            for char in charMap[digit]:
                curr.append(char)
                util(index+1)
                curr.pop()
            return 
        util(0)
        return res