class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        startColor = image[sr][sc]

        if startColor == color: return image

        from collections import deque

        queue = deque([(sr,sc)])
        image[sr][sc] = color

        while queue:
            x, y = queue.popleft()
            for i, j in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+i, y+j
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == startColor:
                    queue.append((nx,ny))
                    image[nx][ny] = color
        return image
