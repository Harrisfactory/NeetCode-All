class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        #storing s in dictionary, assigning t[i] value for each s key, if differ, fail, if not, pass
        iso_dict = {}
        for i in range(len(s)):
            if s[i] in iso_dict:
                #if val is mapped from s key to t val
                if iso_dict[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                #the value is already mapped to another key
                if t[i] in iso_dict.values():
                    return False
                iso_dict[s[i]] = t[i]

        return True

        #has runtime O(n) where n is number of elements in string s