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
            
            if ans * 10 + lastDigit > maxInt:
                print(ans * 10 + lastDigit , maxInt)
                return 0
            if ans * 10 + lastDigit > minInt:
                
                return 0
            ans = ans * 10 + lastDigit
            x = x // 10
        return sign * ans 
