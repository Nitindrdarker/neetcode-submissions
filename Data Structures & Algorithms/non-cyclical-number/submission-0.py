class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        num = n
        while num > 1:
            s = 0
            n = num
            while n > 0:
                last = n % 10
                last = last * last
                s += last
                n = n // 10
            if s in seen:
                return False
            seen.add(s)
            num = s
        return True
            
            
        