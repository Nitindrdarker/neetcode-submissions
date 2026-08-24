class Solution:
    def addBinary(self, s: str, t: str) -> str:
        carry = 0
        res = ''
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            a = int(s[i]) if i >= 0 else 0
            b = int(t[j]) if j >= 0 else 0
            val = a ^ b ^ carry
            res = str(val) + res
            carry = 1 if a + b + carry > 1 else 0
            i -= 1
            j -= 1
        if carry > 0:
            return "1" + res
        return res
            

        



            
