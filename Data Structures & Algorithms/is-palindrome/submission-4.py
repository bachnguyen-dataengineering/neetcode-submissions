class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        n = len(s)
        print(s)
        for i in range(n):
            j = n-1-i
            if s[i] != s[j]:
                return False
        return True