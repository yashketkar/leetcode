# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
        	return ""
        build = str(t.val)
        if t.left is not None or t.right is not None:
	        build += "(" + self.tree2str(t.left) + ")"
        if t.right is not None:
	        build += "(" + self.tree2str(t.right) + ")"
        return build
