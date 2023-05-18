class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        unique = set()

        left = 0
        right = 0

        max_longest = 0

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                max_longest = max(max_longest, len(unique))
                right+=1
            elif s[right] in unique:
                max_longest = max(max_longest, len(unique))
                unique.remove(s[left])
                left+=1


        return max_longest

        #runtime is O(n) as each element in s is iterated through

        #sliding window technique