class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #I want to buy as low as possible and sell as high as possible

        #sliding window technique: I compare the two pointers and move the left to the right if a new right would make a better left than current left

        if len(prices) == 1:
            return 0

        max_profit = 0

        left = 0
        right = 0

        while right < len(prices):
            max_profit = max(prices[right]-prices[left], max_profit)
            if prices[left] <= prices[right]:
                right+=1
            else:
                left=right
                right+=1

        return max_profit

        #runtime is O(n) worst case the elements are descending and we iterate over each element