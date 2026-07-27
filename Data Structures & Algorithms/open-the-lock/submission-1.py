class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def forward(val, i):
            v = val[:i] + str((int(val[i]) + 1) % 10) + val[i+1:]
            return v
        def backward(val, i):
            v = val[:i] + str((int(val[i]) - 1 + 10) % 10) + val[i+1:]
            return v

            
            
            
            
            
        s = set(deadends)
        if '0000' in s or target in s:
            return -1
        q = collections.deque()
        q.append(('0000', 0))
        visited = set()
        while q:
            node, count = q.popleft()
            if node == target:
                return count
            if node in visited:
                continue
            visited.add(node)
            # forward
            for i in range(4):
                fw = forward(node, i)
                bw = backward(node, i)
                if fw not in s and fw not in visited:
                    q.append((fw, count + 1))
                if bw not in s and bw not in visited:
                    q.append((bw, count + 1))

        return -1
                
                    

            
            

