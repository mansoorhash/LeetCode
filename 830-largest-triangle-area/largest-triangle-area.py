class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        max_area = 0
        n_size = len(points)
        for i in range(n_size):
            for j in range(i+1,n_size):
                for k in range(j+1, n_size):
                    x, y = points[i]
                    x1, y1 = points[j]
                    x2, y2 = points[k]
                    
                    area = abs(x*(y1-y2) + x1*(y2-y) + x2*(y-y1))/2
                    max_area = max(area, max_area)
            
        return max_area