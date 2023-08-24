import numpy
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        unique_multi = {}

        result = []

        for i in range(len(nums)):
            number = nums[i]
            if number not in unique_multi:
                unique_multi[number] = numpy.prod(nums[:i] + nums[i + 1:])
            result.append(unique_multi[number])

        return result
    
    #O(n)