# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.is_mirror(root.left, root.right)

    def is_mirror(self, a, b):
        if not a and not b:
            return True
        if (not a and b) or (not b and a) or (a.val != b.val):
            return False
        return self.is_mirror(a.left, b.right) and self.is_mirror(a.right, b.left)
