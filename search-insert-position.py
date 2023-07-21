class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0

        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        #search should only have 1 element left 
        return left

        #O(log(n)) search field shrinks after each iteration