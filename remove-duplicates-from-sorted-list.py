# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #declare unique, if unique == val, remove, else assign unique cont

        if head == None:
            return None

        unique = None

        current_node = head
        while current_node is not None and current_node.next is not None:

            if current_node.val == unique and prev:
                tmp = current_node
                current_node = prev
                current_node.next = tmp.next
                unique = current_node.val
            else:
                unique = current_node.val

            prev = current_node
            current_node = current_node.next
        #case for match at end of list
        if current_node.val == unique:
            current_node = prev
            current_node.next = None

        return head