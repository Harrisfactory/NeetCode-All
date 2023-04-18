class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #plan: sort alpha, store in dict if doesnt exist, append unsorted to value, return values

        unclean_result = {}

        result = []

        for word in strs:
            if ''.join(sorted(word)) in unclean_result:
                unclean_result[''.join(sorted(word))].append(word)
            else:
                unclean_result[''.join(sorted(word))] = [word]

        for k in unclean_result:
            result.append(unclean_result[k])

        return result