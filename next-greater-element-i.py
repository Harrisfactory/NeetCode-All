class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #cycle through nums1
        #foreach nums1[i], find nums2[j]
        #cycle through from nums2[i] look for larger elem to the right,
        #if none add -1 to nums1[i] else add larger elem to nums1[i]
        #return nums1

        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[j] > nums1[i]:
                    nums1[i] = nums2[j]
                    break
                elif j == len(nums2)-1:
                    nums1[i] = -1
        return nums1
            

        #runtime is O(n^2)