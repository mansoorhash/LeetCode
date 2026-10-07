class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque

        q = deque()

        ROW, COL = len(board), len(board[0])

        visited = set()
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != "O" or (r,c) in visited:
                    continue
                q.append((r,c))
                valid = False
                circles = []
                while q:
                    x, y = q.popleft()
                    circles.append((x,y))
                    if x == 0 or x == ROW-1 or y == 0 or y == COL -1:
                        valid = True
                    for i, j in ((1,0),(-1,0),(0,1),(0,-1)):
                        new_r, new_c = x + i, y+j
                        if 0 <= new_r < ROW and 0 <= new_c < COL and board[new_r][new_c] == "O" and (new_r, new_c) not in visited:
                            visited.add((new_r, new_c))
                            q.append((new_r, new_c))
                if not valid:
                    for x,y in circles:
                        board[x][y] = "X"