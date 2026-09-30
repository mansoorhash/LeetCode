# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        base = None

        def dfs(node, min_value=float('-inf'), max_value=float("inf")):
            if not node: return True
            if min_value >= node.val or node.val >= max_value:
                return False
            return dfs(node.left, min_value=min_value, max_value=node.val) \
            and dfs(node.right, min_value=node.val, max_value=max_value)
                
        return dfs(root)
