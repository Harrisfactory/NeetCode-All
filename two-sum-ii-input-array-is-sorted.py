class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0

        right = len(numbers) - 1

        solution = []

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right-=1
            else:
                left+=1

        return [left,right]

        #runtime is O(n) if the target is large enough you will need to iterate to the end of the list