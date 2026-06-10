class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #find the top value
        left = 0
        n = mountainArr.length()
        right = n
        cache = {}

        def getVal(index):
            if index in cache:
                return cache[index]
            v = mountainArr.get(index)
            cache[index] = v
            return v

        while left < right:
            mid = left + (right - left) // 2
            val = getVal(mid)
            rVal = getVal(mid + 1)
            
            if val < rVal:
                left = mid + 1
            else:
                right = mid
        top = left
        left = 0
        right = top
        while left <= right:
            mid = left + (right - left) // 2
            val = getVal(mid)
            if val == target:
                return mid
            elif target > val:
                left = mid + 1
            else:
                right = mid - 1
        left = top
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = getVal(mid)
            if val == target:
                return mid
            elif val < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        
        


