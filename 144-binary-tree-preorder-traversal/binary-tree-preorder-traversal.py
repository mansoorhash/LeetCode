# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            r = []
            r.append(node.val)
            r.extend(dfs(node.left))
            r.extend(dfs(node.right))
            return r
        return dfs(root)
            
            
            