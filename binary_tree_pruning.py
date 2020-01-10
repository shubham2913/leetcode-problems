# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def count_1(self,root) :
        if root!=None :
            count=0
            if root.val==1 :
                count+=1
            count+=self.count_1(root.left)
            count+=self.count_1(root.right)
            return count
        else :
            return 0
    def pruneTree(self, root):
        if root!=None :
            if root.left!=None :
                nleft=self.count_1(root.left)
                if nleft==0 :
                    root.left=None
                self.pruneTree(root.left)
            if root.right!=None :
                nright=self.count_1(root.right)
                if nright==0 :
                    root.right=None
                self.pruneTree(root.right)
            return root
        else :
            return None