class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pos_s = 0

        if s == "":
            return True
        if len(s) == len(t):
            if s == t:
                return True
            else:
                return False

        for i in range(len(t)):
            if s[pos_s] == t[i]:
                pos_s+=1
                if pos_s == len(s):
                    return True

        if pos_s == len(s):
            return True

        return False
    #solution is O(n) where n is length of t as we only cycle through elements of t once