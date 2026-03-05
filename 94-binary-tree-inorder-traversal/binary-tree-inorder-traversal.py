# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def dfs(tree=None):
            if not tree: return
            dfs(tree.left)
            l.append(tree.val)
            dfs(tree.right)
            
        dfs(root)
        return l
                 

        