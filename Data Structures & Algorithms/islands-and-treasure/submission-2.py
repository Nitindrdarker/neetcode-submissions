class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647

        row = len(grid)
        col = len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        q = collections.deque()

        for i in range(row):
            for j in range(col):
                # find the treasure
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            i, j, d = q.popleft()
            if grid[i][j] == inf:
                grid[i][j] = d
            
            for a, b in neighbors:
                r, c = i + a, j + b
                if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != inf:
                    continue
                q.append((r, c, d + 1))
        
            


                



        