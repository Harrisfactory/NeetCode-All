class Solution:
    def arraySign(self, nums: List[int]) -> int:

        result = prod(nums)

        if result > 0:
            return 1
        if result < 0:
            return -1
        return 0