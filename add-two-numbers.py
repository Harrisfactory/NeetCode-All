# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #numbers are reversed

        #return as a linked list, reversed

        cur = l1

        l1_list = ''
        l2_list = ''

        while cur != None:
            l1_list+=str(cur.val)
            cur = cur.next
        cur = l2
        while cur != None:
            l2_list+=str(cur.val)
            cur = cur.next

        l1_rev = int(l1_list[::-1])
        l2_rev = int(l2_list[::-1])

        

        fin = list(str(l1_rev+l2_rev))


        print(fin)

        head = ListNode(fin[-1])

        cur = head

        for i in reversed(range(len(fin) - 1)):
            cur.next = ListNode(fin[i])
            cur = cur.next
        

        return head

        #complexity O(n + m + n + m + nm + k)
