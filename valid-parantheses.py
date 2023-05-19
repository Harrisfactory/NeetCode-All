class Solution:
    def isValid(self, s: str) -> bool:

        #build dict: keys being lbracks, values being rbracks
        #create lbrack string
        #create rbrack string

        #store lbracks onto stack, if rbrack encountered, pop lbrack and compare validity

        #make sure stack is empty at end


        brack_dict = {'(':')','{':'}','[':']'}

        l_brack = '({['
        r_brack = ')}]'

        brack_stack = []

        for i in range(len(s)):
            if s[i] in r_brack:
               if len(brack_stack) == 0 or brack_dict[brack_stack.pop()] != s[i]:
                   return False
            else:
                brack_stack.append(s[i])

        if len(brack_stack) > 0:
            return False

        return True

        #runtime is O(n) where n is the number of chars in the string s