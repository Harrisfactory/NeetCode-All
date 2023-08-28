class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)

        left = 0

        right = window

        search1 = sorted(s1)

        while right <= len(s2):
            search2 = sorted(s2[left:right])
            if search1 == search2:
                return True
            else:
                left+=1
                right+=1

        return False