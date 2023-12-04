# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        #a leaf is a node with no children

        path = []
        
        #implementing backtracking to find a sum that matches
        def inorder(root, path):
            #fail case
            if root is None:
                return False
            
            #candidate for successful path
            path.append(root.val)

            if sum(path) == targetSum and root.left is None and root.right is None:
                return True
            
            if inorder(root.left, path):
                return True
            if inorder(root.right, path):
                return True

            path.pop()
            return False
            
        res = inorder(root, path)

        return res

