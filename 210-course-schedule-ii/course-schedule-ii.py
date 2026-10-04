class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pre = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            pre[crs].append(preq)

        order = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True
            cycle.add(crs)

            for p in pre[crs]:
                if dfs(p) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        for n in range(numCourses):
            if dfs(n) == False:
                return []

        return order
                


