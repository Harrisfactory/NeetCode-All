    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        solution = []

        notintwo = []

        notinone = []

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in notintwo:
                notintwo.append(nums1[i])
        solution.append(notintwo)
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in notinone:
                notinone.append(nums2[i])
        solution.append(notinone)
        return solution

        #O(n + n)