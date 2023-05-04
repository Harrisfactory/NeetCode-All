class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counter = {}
        for number in nums:
            if number in num_counter:
                num_counter[number]+=1
            else:
                num_counter[number]=1
        return max(num_counter, key=num_counter.get)
        #runtime is O(n+n) where n is number of elements in nums