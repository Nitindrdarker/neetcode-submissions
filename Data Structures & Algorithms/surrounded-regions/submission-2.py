class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    if board[i][j] == "O":
                        q.append((i, j))
        
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            i, j = q.popleft()
            board[i][j] = '@'
            for dy, dx in neighbors:
                nr, nc = i + dy, j + dx
                if nr >= row or nc >= col or nr < 0 or nc < 0:
                    continue
                if board[nr][nc] == "O":
                    q.append((nr, nc))
        for i in range(row):
            for j in range(col):
                if board[i][j] != '@':
                    board[i][j] = "X"
                elif board[i][j] == '@':
                    board[i][j] = 'O'
        

