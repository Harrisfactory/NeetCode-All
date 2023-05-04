class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #collect each num in dictionary and count as its value

        #then decrement k by each max from dict, then remove that max

        #k is atleast 1
        result = []

        num_counter = {}

        for number in nums:
            if number in num_counter:
                num_counter[number]+=1
            else:
                num_counter[number] = 1
        
        while k > 0:
            cur_max = max(num_counter, key=num_counter.get)
            result.append(cur_max)
            del num_counter[cur_max]
            k-=1
        
        return result

        #runtime is O(n+k) where n is number of elements in nums