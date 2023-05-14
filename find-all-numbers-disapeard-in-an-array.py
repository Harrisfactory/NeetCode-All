class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        solution = []

        num_dict = {}

        ctr = 1

        #loop through and store list as dictionary
        #we can search and access the dictionary by length,
        #each search will give us O(1) instead of O(n) which
        #should give us a fast enough runtime

        for number in nums:
            if number in num_dict:
                continue
            else:
                num_dict[number] = 1
        
        while ctr < len(nums) + 1:
            if ctr not in num_dict:
                solution.append(ctr)
            ctr+=1
        
        return solution

        #runtime is O(n + n) where n is the number of elements in nums