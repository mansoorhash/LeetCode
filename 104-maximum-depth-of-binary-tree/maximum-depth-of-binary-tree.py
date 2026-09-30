# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, c=1):
            if not node: return 0
            left_c = 0
            right_c = 0
            if node.left:
                left_c += dfs(node.left)
            if node.right:
                right_c += dfs(node.right)
            return max(left_c+c, right_c+c)
        return dfs(root)
