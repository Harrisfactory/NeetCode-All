# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #intuitive approach just stack and unstack O(n + n)
        #if head is None:
        #    return None

        #stack: List[ListNode] = []

        #cur = head

        #while cur != None:
        #    stack.append(cur.val)
        #    cur = cur.next
        
        #new_head = ListNode(stack.pop())
        #new_cur = new_head
        #while len(stack) > 0:
        #    new_cur.next = ListNode(stack.pop())
        #    new_cur = new_cur.next
            
        #return new_head

        #optimal approach

        prev = None
        while head is not None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
        return prev