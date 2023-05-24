# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def preorder(root):
            if root:
                result.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)

        return result

        #space O(h) where h is height of tree
        #runtime is O(n) where n is number of nodes in tree