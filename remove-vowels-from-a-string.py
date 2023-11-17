class Solution:
    def removeVowels(self, s: str) -> str:

        vowels = {"a","e","i","o","u"}

        ctr = 0

        fin: str = ''

        while ctr < len(s):
            if s[ctr] not in vowels:
                fin += s[ctr]
            ctr+=1
        return fin