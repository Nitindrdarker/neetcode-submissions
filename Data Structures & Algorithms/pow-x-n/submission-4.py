class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1
        isInverse = False
        if n < 0:
            isInverse = True
            n = -1 * n
        if x < 0 and n % 2:
            sign = -1
            

        def calc(p):
            if p <= 0:
                return 1
            if p == 1:
                return x
            val = calc(p // 2)
            if p % 2:
                return x * val * val
            return val * val
        v = calc(n)
        if isInverse:
            v = 1 / v
        return v
