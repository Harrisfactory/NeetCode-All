class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return 1
        

        #sliding window: reason: because I see where I can snap and continue

        #plan I can add repitions to a set and compare current count to a max count

        #If I repeat a char in this cycle I snap to that point and move end over one

        #return max count

        max_char_count: int = 0

        non_repeated_chars = [s[0]]

        start, end = 0, 1

        cur_char_count: int = 1

        while end < len(s):
            #fail case
            if s[end] in non_repeated_chars:
                start+=1
                #pop start
                non_repeated_chars.pop(0)
                max_char_count = max(max_char_count, cur_char_count)
                cur_char_count-=1
                continue
             
            non_repeated_chars.append(s[end])
            end+=1
            cur_char_count+=1
            max_char_count = max(max_char_count, cur_char_count)
            

        return max_char_count

        #O(n) I go through the elements once
