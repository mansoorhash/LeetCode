# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, left=False):
            if not node: return 0
            s = 0
            if node.left is None and node.right is None:
                return node.val if left else 0

            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root)
            
