class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHash = {}

        for s in strs:
            s2 = ''.join(sorted(s))

            if s2 not in anagramHash:
                anagramHash[s2] = []
            anagramHash[s2].append(s)
        
        return list(anagramHash.values())