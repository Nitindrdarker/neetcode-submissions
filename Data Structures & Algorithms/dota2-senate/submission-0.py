class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = 0
        d = 0
        q = collections.deque()
        for i in senate:
            q.append(i)
            if i == 'D':
                d += 1
            else:
                r += 1
        removeD = removeR = 0
        
        while r and d:
            v = q.popleft()
            if v == 'D':
                if removeD:
                    removeD -= 1
                    d -= 1
                else:
                    removeR += 1
                    q.append(v)
            else:
                if removeR:
                    removeR -= 1
                    r -= 1
                else:
                    removeD += 1
                    q.append(v)
        return "Radiant" if r else "Dire"