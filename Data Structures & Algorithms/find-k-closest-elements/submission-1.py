class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        center = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                center = mid
                left = mid + 1
            else:
                right = mid - 1
        
        
        if center + 1 < len(arr) and  arr[center + 1] - x < x - arr[center]:
            center += 1
        
        
        left = center
        
        right = center
        
        while right - left + 1 < k:
            if left == 0:
                right += 1
            elif right == len(arr) - 1:
                left -= 1
            else:
                if abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                    left -= 1
                else:
                    right += 1
        
        return arr[left: right + 1]
        
        