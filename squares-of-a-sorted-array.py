class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right = 0, len(nums) - 1

        while left<=right:
            nums[left], nums[right] = nums[left]*nums[left], nums[right]*nums[right]
            left+=1
            right-=1
        
        return sorted(nums)

        #O(log(n) + nlog(n))