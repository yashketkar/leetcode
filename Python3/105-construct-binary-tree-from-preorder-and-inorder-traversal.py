# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dic = {data:i for i, data in enumerate(inorder)}
        root = self.helper(preorder, inorder, dic, 0, len(preorder), 0, len(inorder))
        return root

    def helper(self, preorder, inorder, dic, pi, pj, ii, ij):
        if pj <= pi or ij <= ii:
            return None
        i = dic[preorder[pi]]
        left_size = i - ii
        root = TreeNode(preorder[pi])
        root.left = self.helper(preorder, inorder, dic, pi+1, pi+1+left_size, ii, i)
        root.right = self.helper(preorder, inorder, dic, pi+1+left_size, pj, i+1, ij)
        return root
