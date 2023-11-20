# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        #latest version fails quality check

        #each version is developed based on the previous version, so all versions after the first bad version are also bad

        #we are given a range of numbers and we want to make a guess so we need to implement binary search range method. 

        #construct bounds first

        left, right = 0, n

        #our winning number would be if mid is True BUT mid - 1 is False


        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == False:# middle is still good, drag left to mid
                left = mid + 1
            else:#middle is bad and 1 before is not good, drag right to mid
                right = mid - 1