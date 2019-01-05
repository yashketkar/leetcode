# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_balanced(root) > -1

    def is_balanced(self, node):
        if not node:
            return 0
        left_height = self.is_balanced(node.left)
        if left_height == -1:
            return -1
        right_height = self.is_balanced(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return (1 + max(left_height, right_height))
