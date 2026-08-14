class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        prev = 0
        count = 1
        res = 1

        for i in range(1, len(arr)):
            curr = 1 if arr[i - 1] < arr[i] else -1 if arr[i - 1] > arr[i] else 0

            if curr == 0:
                count = 1
            elif curr != prev:
                count += 1
            else:
                count = 2

            prev = curr
            res = max(res, count)
        return res