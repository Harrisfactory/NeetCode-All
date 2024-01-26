class Solution:
    def removeStars(self, s: str) -> str:

        #looks like a stack problem, i would simply add to stack as I cycle, if I encounter a start i pop then continue to next iter, then I return the stack as a string


        result_stack = []
        res_str = ''

        for i in range(len(s)):
            if s[i] == '*':
                result_stack.pop()
                continue
            result_stack.append(s[i])

        for char in result_stack:
            res_str += char
        
        return res_str
