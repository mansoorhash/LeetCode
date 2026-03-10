# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node: return []
            r = []
            r.extend(dfs(node.left))
            r.extend(dfs(node.right))
            r.append(node.val)
            return r
        return dfs(root)
        