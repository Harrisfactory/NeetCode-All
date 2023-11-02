class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_ct = 0

        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                zero_ct+=1
                del nums[i]
        while zero_ct > 0:
            nums.append(0)
            zero_ct-=1