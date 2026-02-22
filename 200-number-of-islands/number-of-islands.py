class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        from collections import deque
        

        rowSize = len(grid)
        colSize = len(grid[0])

        for r in range(rowSize):
            for c in range(colSize):
                if grid[r][c] == "1":
                    islands += 1
                    queue = deque([(r,c)])
                    grid[r][c] = "0"

                    while queue:
                        i, j = queue.popleft()

                        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                            m, n = i+di, dj+j
                            if 0 <= m < rowSize and 0<= n < colSize:
                                if grid[m][n] == "1":
                                    grid[m][n] = "0"
                                    queue.append((m,n))
        return islands