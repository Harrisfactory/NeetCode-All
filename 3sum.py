class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        unique_threes = set()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j <= k:
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i],nums[j],nums[k]) not in unique_threes:
                        unique_threes.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
                    k-=1
        return unique_threes
