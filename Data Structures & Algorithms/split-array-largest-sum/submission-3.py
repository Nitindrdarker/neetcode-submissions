class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def util(cap):
            count = 0
            weight = 0
            for i in nums:
                if i > cap:
                    return k + 1
                weight += i
                if weight > cap:
                    count += 1
                    weight = i
            if weight > 0:
                count += 1
            return count
        
        left = 1
        right = sum(nums)
        ls = 0
        while left <= right:
            mid = (left + right) // 2
            
            count = util(mid)
            if count <= k:
                ls = mid
                right = mid - 1
            else:
                left = mid + 1
        return ls



        


                



            
        