class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pre = {crs: [] for crs in range(numCourses)}
        for a, b in prerequisites:
            pre[a].append(b)
        order = []
        takenCourse = set()
        loop = set()

        def dfs(crs):
            if crs in takenCourse: return True
            if crs in loop: return False
            loop.add(crs)

            for c in pre[crs]:
                if dfs(c) == False:
                    return False
            
            loop.remove(crs)
            takenCourse.add(crs)
            order.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c): return []
        return order
                


