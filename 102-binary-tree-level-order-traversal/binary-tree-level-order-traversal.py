# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        if not root: return []
        q = deque([root])
        result = []
        while q:
            nodes_floor = len(q)
            result.append([])
            for _ in range(nodes_floor):
                node = q.popleft()
                result[-1].append(node.val)
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
        return result



