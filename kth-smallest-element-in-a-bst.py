# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #plan: until k == 1 find and return

        #inorder, dec 1 from k until k == 1 then return val

        result = None

        def inorder(root):
            nonlocal k, result

            if root:
                inorder(root.left)
                k-=1
                if k == 0:
                    result = root.val
                    return
                inorder(root.right)
        inorder(root)

        return result
