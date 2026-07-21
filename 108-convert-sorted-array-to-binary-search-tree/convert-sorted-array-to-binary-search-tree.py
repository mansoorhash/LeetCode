# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def sorter(nums):
            if not nums: return None

            nums_length = len(nums)-1
            if nums_length == 0: return TreeNode(val=nums[0])

            midpoint = (nums_length//2)
            left_nums = nums[:midpoint]
            right_nums = nums[midpoint+1:]
            node = TreeNode(val=nums[midpoint], left=sorter(left_nums), right=sorter(right_nums))
            return node
        return sorter(nums)
            
            

        