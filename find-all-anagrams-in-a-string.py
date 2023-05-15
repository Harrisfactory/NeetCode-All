class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        #sort p

        #grab left and right of s based on length of p

        #if subset of s sorted equals p sorted, append left index to result

        #then incriment left and right by 1

        #test again until end

        p = sorted(p)
        left = 0
        right = len(p)
        result = []

        while right <= len(s):
            if (sorted(s[left:right]) == p):
                result.append(left)
            right+=1
            left+=1
        return result

        #runtime is O(n^nlogn) where n is number of elements in s