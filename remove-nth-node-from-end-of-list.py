# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current_node = head
        temp = head
        list_length = 0

        #get length of linked list
        while temp is not None:
            list_length+=1
            temp = temp.next

        target_index = list_length - n

        if list_length == 1:
            return None

        #keeps track of our loop positions
        pos = 0
        
        #aim for the node before the target node
        while current_node is not None and pos+1 < target_index:
            pos+=1
            current_node = current_node.next

        if target_index == 0:
            return current_node.next
        #now at target index, compute removal
        current_node.next = current_node.next.next

        return head


        #beats 75%, O(L1 + L1)