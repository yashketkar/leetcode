# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        all_levels = []
        while queue:
            current_level = []
            next_level = []
            for x in queue:
                current_level.append(x.val)
                if x.left:
                    next_level.append(x.left)
                if x.right:
                    next_level.append(x.right)
            all_levels.append(current_level)
            queue = next_level
        return all_levels
