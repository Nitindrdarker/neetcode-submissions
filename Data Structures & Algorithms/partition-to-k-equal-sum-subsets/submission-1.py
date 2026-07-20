class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        
        target = total // k
        val = [0] * k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        def util(index):
            if index >= len(nums):
                return True
            for i in range(k):
                if val[i] + nums[index] <= target:
                    val[i] += nums[index]
                    if util(index + 1):
                        return True
                    val[i] -= nums[index]
                if val[i] == 0:
                    break
            return False
        return util(0)