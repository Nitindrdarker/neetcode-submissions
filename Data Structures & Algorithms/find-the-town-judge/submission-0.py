class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        vote = {i : [] for i in range(n+1)}
        count = {}
        candidates = []
        for a, b in trust:
            vote[a].append(b)
            count[b] = count.get(b, 0) + 1
            if count[b] == n - 1:
                candidates.append(b)
        
        for i in candidates:
            if len(vote[i]) == 0:
                return i

        return -1

            
             
        
        