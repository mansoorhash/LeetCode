# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, side=None):
            if not node: return 0
            s = 0
            if side == "left" and node.left is None and node.right is None:
                s += node.val
            elif node.left:
                s += dfs(node.left, "left")
            if node.right:
                s += dfs(node.right, "right")
            
            return s
        return dfs(root)
            
