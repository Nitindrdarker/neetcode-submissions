class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 0x7FFFFFFF
        minInt = 0xFFFFFFFF
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        

        ans = 0
        while x != 0:
            lastDigit = x % 10
            if  lastDigit > maxInt - (ans * 10):
                return 0
            if  lastDigit > minInt - (ans * 10):
                return 0
            ans = ans * 10 + lastDigit
            x = x // 10
        return sign * ans 
