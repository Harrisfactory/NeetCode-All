# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #set empty new list
        #set res head to new list node
        #set result and keep it

        #while either list is nonempty
            #if list 1 head nonempty 
                #append 1 to new list
                #move head to next node
            #if list 2 head is nonempty
                #append 2 to new list
                #move head to next node

        #return result

        if not list1 and not list2:
            return None

        sorted_list = ListNode()

        result = sorted_list

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    sorted_list.val = list1.val
                    list1 = list1.next
                else:
                    sorted_list.val = list2.val
                    list2 = list2.next
            elif list1 and not list2:
                sorted_list.val = list1.val
                list1 = list1.next
            elif list2 and not list1:
                sorted_list.val = list2.val
                list2 = list2.next
            
            #if there is a next, extend
            if list1 or list2:
                sorted_list.next = ListNode()
                sorted_list = sorted_list.next

        return result

        #runtime O(list1 + list2)