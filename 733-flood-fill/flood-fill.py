class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        selected_color = int(image[sr][sc])
        from collections import deque

        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            if image[r][c] != color and image[r][c] == selected_color:
                image[r][c] = color
            
                for x, y in ((1,0),(0,1),(-1,0),(0,-1)):
                    new_sr = r + x
                    new_sc = c + y
                    if new_sr < 0 or new_sr > len(image)- 1:
                        continue
                    if new_sc < 0 or new_sc > len(image[0]) - 1:
                        continue
                    if image[new_sr][new_sc] == selected_color:
                        q.append((new_sr, new_sc))

        return image
