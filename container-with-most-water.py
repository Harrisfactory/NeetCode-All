class Solution:
    def maxArea(self, height: List[int]) -> int:

        #want to compare lxh and return the max amount
        left = 0
        right = len(height) - 1

        #calculate inital max volume
        max_volume = min(height[left],height[right])*(right-left)

        while left < right:
            #get current height of water without spill
            cheight = min(height[left],height[right])

            max_volume = max(max_volume,(right-left)*cheight)
        
            if height[left] < height[right]:
                left+=1
            elif height[right] < height[left]:
                right-=1
            else:
                left+=1
                right-=1

        return max_volume
    
    #runtime O(n) because of possibility of one pointer shifting the entire list