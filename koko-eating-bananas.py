class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # n = number of piles of bananas

        # piles[i] is the ith pile of bananas

        #guards left and will come back in h hours

        #koko wants to eat all the bananas before the guards return~~~~

        #if the pile has less than k bananas she will eat all of them but not eat more that hour which is unoptimal

        #return the minimum integer k such that she eat all the bananas within h hours

        #this looks like a binary search range problem

        left, right = 1, max(piles)

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if self.can_eat(mid, piles, h) == True:
                ans = mid
                right = mid - 1
            else: #guards came back too soon, drag left to mid
                left = mid + 1
        
        return ans

    def can_eat(self, mid, piles, h):
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i]/mid)
        if hours <= h:
            return True
        return False