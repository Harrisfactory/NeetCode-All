# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        palindrome = []

        current_node = head

        while current_node:
            palindrome.append(current_node.val)
            current_node = current_node.next

        left, right = 0, len(palindrome) - 1

        while left <= right:
            if palindrome[left] != palindrome[right]:
                return False
            left+=1
            right-=1
        return True

        #complexity O(n + log(n))