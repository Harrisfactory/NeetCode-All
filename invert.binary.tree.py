# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        temp_left = root.left
        root.left = root.right
        root.right = temp_left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        #space is O(h) for height of tree
        #runtime is O(n) for number of elements in tree