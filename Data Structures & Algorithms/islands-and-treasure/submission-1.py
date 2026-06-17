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
        visited = set()
        while q:
            i, j, d = q.popleft()
            if (i, j) in visited:
                continue
            if grid[i][j] == inf:
                grid[i][j] = d
            visited.add((i, j))
            
            for a, b in neighbors:
                r, c = i + a, j + b
                if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == -1 or (r, c) in visited:
                    continue
                q.append((r, c, d + 1))
        
            


                



        