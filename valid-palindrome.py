class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s)==1:
            return True

        left = 0

        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum() and s[left].lower() == s[right].lower():
                right-=1
                left+=1
            elif s[left].isalnum() and s[right].isalnum() and s[left].lower() != s[right].lower():
                return False
            if not s[left].isalnum():
                left+=1
            if not s[right].isalnum():
                right-=1
        
        return True

        #runtime is O(n) as there is a chance that we will have to iterate every character checking for letters