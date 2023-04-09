class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1 or strs[0] == "":
            return strs[0]

        first_word = strs[0]

        cur_char = 0

        result = ''

        while cur_char < len(first_word):
            for word in strs[1:len(strs)]:
                if first_word[cur_char] and cur_char < len(word) and first_word[cur_char] == word[cur_char]:
                    continue
                else:
                    return result
            result += first_word[cur_char]
            cur_char+=1
            
        return result