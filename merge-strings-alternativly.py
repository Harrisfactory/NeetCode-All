class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        w1_ctr = 0
        w2_ctr = 0
        result = ''

        while w1_ctr < len(word1) or w2_ctr < len(word2):
            if w1_ctr < len(word1):
                result+=word1[w1_ctr]
                w1_ctr+=1
            if w2_ctr < len(word2):
                result+=word2[w2_ctr]
                w2_ctr+=1
        return result