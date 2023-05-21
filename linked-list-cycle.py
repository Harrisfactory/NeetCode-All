# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #store each node in dictionary with its key being its next node

        known_nodes = set()

        while head:
            if head in known_nodes:
                return True
            known_nodes.add(head)
            head = head.next
        return False