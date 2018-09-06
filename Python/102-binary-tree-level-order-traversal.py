# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        final = []
        successors = [root]
        while successors:
            final.append([s.val for s in successors])
            next_successors = []
            for s in successors:
                if s.left:
                    next_successors.append(s.left)
                if s.right:
                    next_successors.append(s.right)
            successors = next_successors
        return final
