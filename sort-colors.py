class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        self.mergeSort(nums)

        return nums

    
    def mergeSort(self, nums):
        if len(nums) > 1:

            mid = len(nums) // 2
            #split into halves
            left = nums[:mid]
            right = nums[mid:]
            #recursivly sort each side
            self.mergeSort(left)
            self.mergeSort(right)

            #sorting logic
            i,j,k = 0,0,0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i+=1
                else:
                    nums[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                nums[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                nums[k] = right[j]
                j+=1
                k+=1
            