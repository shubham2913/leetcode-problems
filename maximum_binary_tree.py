# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums) :
        if len(nums)==1 :
            node=TreeNode(nums[0])
            return node
        else :
            root_value=max(nums)
            root_index=nums.index(root_value)
            root=TreeNode(root_value)
            if root_index==0 :
                root.right=self.constructMaximumBinaryTree(nums[1:])
            elif root_index==len(nums)-1 :
                root.left=self.constructMaximumBinaryTree(nums[0:-1])
            else :
                root.left=self.constructMaximumBinaryTree(nums[0:root_index])
                root.right=self.constructMaximumBinaryTree(nums[root_index+1:])
            return root