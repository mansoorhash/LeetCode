class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def dfs(i, curr, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                results.append(curr.copy())
                return
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return results