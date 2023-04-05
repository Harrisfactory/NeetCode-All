class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            potential = target - nums[i]

            print(potential)
            if potential in nums and potential + nums[i] == target and i != nums.index(potential):
                return [i, nums.index(potential)]