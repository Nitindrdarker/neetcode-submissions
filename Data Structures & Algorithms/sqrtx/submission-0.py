class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res

                

        