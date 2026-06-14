class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        linked_s = {}
        for s1 in s:
            if s1 not in linked_s:
                linked_s[s1] = 1
            else:
                linked_s[s1] += 1
        
        for t1 in t:
            if t1 not in linked_s:
                return False
            else:    
                linked_s[t1] -= 1
        
        for s1 in linked_s:
            if linked_s[s1] >= 1:
                return False
        return True
            