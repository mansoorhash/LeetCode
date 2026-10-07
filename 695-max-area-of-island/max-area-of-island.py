class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        result = 0
        from collections import deque

        q = deque([])
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    q.append((r,c))
                    curr_island = 0
                    while q:
                        curr_island += 1
                        x,y = q.popleft()
                        grid[x][y] = 0
                        for i,j in ((1,0),(0,1),(-1,0),(0,-1)):
                            new_r, new_c = x+i, y+j

                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                                q.append((new_r, new_c))
                                grid[new_r][new_c] = 0
                    result = max(result, curr_island)

        return result



