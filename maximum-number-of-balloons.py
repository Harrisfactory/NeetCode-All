class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        #create dictionary for each balloon char
        #store its occurances as values

        #loop through and build balloons until a count hits 0,
        #count each time a balloon is built, wipe out the built balloon
        #if any value hits zero return counted balloons

        balloon_dict = {}

        for char in text:
            if char in balloon_dict:
                balloon_dict[char]+=1
            elif char in "balon" and char not in balloon_dict:
                balloon_dict[char]=1
        
        empty_flag = 0
        bln_builder = ""
        bln_count = 0

        while empty_flag != 1:
            for char in "balloon":
                if char in balloon_dict and balloon_dict[char] > 0:
                    bln_builder = bln_builder+char
                    balloon_dict[char]-=1
                    if bln_builder == "balloon":
                        bln_count+=1
                        bln_builder = ""
                else:
                    empty_flag = 1
                    break

        return bln_count

        #runtime is O(n + b^d) where n is number of chars in string, and b is number of chars in balloon and d is the number of chars in the balloon dictionary

