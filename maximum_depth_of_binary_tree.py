# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        depth=0
        if root==None :
            return 0
        queue=[(root,1)]
        while len(queue) > 0 :
            node=queue.pop(0)
            if node[1] > depth :
                depth+=1
            if node[0].left != None :
                queue.append((node[0].left,node[1]+1))
            if node[0].right != None :
                queue.append((node[0].right,node[1]+1))
        return depth