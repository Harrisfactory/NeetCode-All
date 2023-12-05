class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        unique_dict = {}
        for i in range(len(nums)):
            if nums[i] in unique_dict:
                unique_dict[nums[i]]+=1
            else:
                unique_dict[nums[i]]=1
        
        for key, val in unique_dict.items():
            if val == 1:
                return key

        return -1

        #O(n+n) linear, could probably improve this
