class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)
        res = right
        def count(cap):
            c = 0
            temp = 0
            for i in weights:
                if i > cap:
                    return days + 1
                c += i
                if c > cap:
                    c = i
                    temp += 1
            if temp > 0:
                temp += 1
            return temp
        while left <= right:
            mid = (left + right) // 2
            c = count(mid)
            
            if c <= days:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res





                
