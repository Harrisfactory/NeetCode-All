class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #merge array 2 into array 1
        ctr = 0
        for i in range(m, m + n):
            nums1[i] = nums2[ctr]
            ctr+=1

        #sort
        #for i in range(len(nums1)):
        #    for j in range(len(nums1)):
        #        if nums1[j] > nums1[i]:
        #            nums1[i], nums1[j] = nums1[j], nums1[i]

        self.mergeSort(nums1)

        #merge sort
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid: int = len(nums) // 2
            left: int = nums[:mid]
            right: int = nums[mid:]

            #recursivly break down each side
            self.mergeSort(left)
            self.mergeSort(right)

            #sorting logic
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
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
