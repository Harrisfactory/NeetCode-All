class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #for i in range(len(nums)):
        #    if sum(nums[:i+1]) == sum(nums[i:]):
        #        return i
        #return -1


        #alternative faster solution
        leftsum = 0
        for i in range(len(nums)):
            leftsum+=nums[i]
            if leftsum == sum(nums[i:]):
                return i
        return -1