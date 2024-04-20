class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window_l = 0
        window_r = k

        cur_sum = sum(arr[window_l:window_r])

        result = 0

        while window_r <= len(arr):
            if (cur_sum / k) >= threshold:
                 result+=1
            #move left and right pointers
            window_l+=1
            window_r+=1
            if window_r < len(arr):
                #remove sum from prev pointer
                cur_sum-=arr[window_l - 1]
                #add sum to new pointer
                cur_sum+=arr[window_r - 1]
        return result
