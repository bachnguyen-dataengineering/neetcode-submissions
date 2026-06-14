class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s2 = sorted(s)
        t2 = sorted(t)
        print(s2)
        print(t2)
        for i in range(len(s2)):
            if s2[i] != t2[i]:
                return False
        return True
                    