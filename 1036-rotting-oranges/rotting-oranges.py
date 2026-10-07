class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque

        q = deque()
        minutes, fresh = 0, 0
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for x, y in ((1,0),(-1,0),(0,1),(0,-1)):
                    new_r, new_c = i + x, j + y
                    if 0 <= new_r < ROW and 0 <= new_c < COL and grid[new_r][new_c] == 1:
                        fresh -= 1
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2
        return minutes if fresh == 0 else -1
            
        
        

            