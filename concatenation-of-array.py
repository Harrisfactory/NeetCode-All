class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        return nums + nums
        #O(n + n): where n is the length of nums, python has to walk this list twice to build the new list 