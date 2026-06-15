class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        candidates.sort()
        def util(index, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if currSum > target:
                return
            if index >= len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                util(i + 1, currSum + candidates[i])
                curr.pop()
        
        util(0, 0)
        return res
        
            

