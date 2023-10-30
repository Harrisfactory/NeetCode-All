class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        org_mag = {}

        for i in range(len(magazine)):
            if magazine[i] in org_mag:
                org_mag[magazine[i]]+=1
            else:
                org_mag[magazine[i]] = 1
        
        for letter in ransomNote:
            if letter in org_mag and org_mag[letter] > 0:
                org_mag[letter]-=1
            else:
                return False
 
        return True