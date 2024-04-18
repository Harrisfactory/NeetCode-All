# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        ltree = root.left
        rtree = root.right

        result = self.inverseSameTree(ltree, rtree)

        return result
    

    def inverseSameTree(self, ltree, rtree):

        if ltree is None and rtree is None:
            return True
        elif ltree is None or rtree is None:
            return False
        
        if ltree.val != rtree.val:
            return False
        return self.inverseSameTree(ltree.left, rtree.right) and self.inverseSameTree(ltree.right, rtree.left)

        return True
