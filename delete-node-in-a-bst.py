# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMin(self, root):
        curNode = root
        while curNode and curNode.left:
            curNode = curNode.left
        return curNode
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:     

        #binary search
        #base case is if we find our target value
        if root is None:
            return None
        #search for the key
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:#key found
            #check for 1 node solutions
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else: #2 node solution
                minNode = self.findMin(root.right)
                #set minimum in deleted node
                root.val = minNode.val
                #now remove old minumum node
                root.right = self.deleteNode(root.right, minNode.val)


        return root
