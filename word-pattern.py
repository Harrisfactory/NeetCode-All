class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        bijection_map = {}

        s = s.split()

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in bijection_map:
                #check if val s matches bijection
                if bijection_map[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in bijection_map.values():
                    return False
                bijection_map[pattern[i]] = s[i]

        return True

        #runtime is O(n^2) where n is the number of elements in the pattern