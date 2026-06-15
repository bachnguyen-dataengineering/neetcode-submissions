class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarPairs2 = set()
        for word1, word2 in similarPairs:
            similarPairs2.add((word1, word2))
            similarPairs2.add((word2, word1))
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            elif (sentence1[i],sentence2[i]) in similarPairs2:
                continue
            else:
                return False
        return True

        
