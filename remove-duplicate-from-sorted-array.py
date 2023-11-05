class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique = set()

        for i in reversed(range(len(nums))):
            if nums[i] in unique:
                del nums[i]
            else:
                unique.add(nums[i])
        return len(unique)