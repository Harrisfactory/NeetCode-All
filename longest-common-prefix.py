class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        blueprint: str = strs[0]

        ctr: int = 0

        while ctr < len(blueprint):
            for word in strs:
                if ctr >= len(blueprint) or ctr >= len(word) or blueprint[ctr] != word[ctr]:
                    return blueprint[:ctr]
            ctr+=1
        
        return blueprint
