# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def countDepth(root, count):
            if root is None:
                return count - 1
            return max(countDepth(root.left, count + 1), countDepth(root.right, count + 1))
        return countDepth(root, 1)