class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}

        for number in nums:
            if number in dup_dict:
                return True
            else:
                dup_dict[number] = 1
        
        return False