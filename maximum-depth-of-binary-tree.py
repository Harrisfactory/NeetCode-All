# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ###################
        #recursive solution
        ###################
        #if not root:#case where root is empty
        #    return 0
        
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #######################
        #iterative BFS solution (level order traversal)
        #######################
        #here we are grabbing each level and incrementing for each level that we can travel
        if not root:
           return 0

        level = 0
        q = deque([root])

        while q:
           for i in range(len(q)):
               node = q.popleft()
               if node.left:
                   q.append(node.left)
               if node.right:
                   q.append(node.right)
           level+=1
        
        return level