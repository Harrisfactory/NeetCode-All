class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ctr = 0

        while ctr < len(nums):
            if nums[ctr] == val:
                del nums[ctr]
                
            else:
                ctr+=1

        return len(nums)

        #O(n) where n is the length of nums as worst case we are cycling through each element of nums