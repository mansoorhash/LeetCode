class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        from collections import deque

        q = deque([])
        for r_idx, row in enumerate(grid):
            for c_idx, val in enumerate(row):
                if val == "1":
                    grid[r_idx][c_idx] = "0"
                    q.append((r_idx, c_idx))
                    islands += 1
                    while q:
                        x, y = q.popleft()
                        for i, j in ((1, 0), (-1,0),(0,-1),(0,1)):
                            new_r = i + x
                            new_c = j + y

                            if 0 > new_r or new_r > len(grid)-1 or 0 > new_c or new_c > len(grid[0]) -1 :
                                continue
                            
                            if grid[new_r][new_c] == "1":
                                grid[new_r][new_c] = "0"
                                q.append((new_r, new_c))
        return islands