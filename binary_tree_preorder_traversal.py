# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def preorderTraversal(self, root):
        if root:
            # self.preorderTraversal(root.left)
            # self.preorderTraversal(root.right)
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else:
            return []