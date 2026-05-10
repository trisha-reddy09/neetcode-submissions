class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(c for c in s if c.isalnum())
        n=len(s)
        for char in range(n//2):
            if s[char] != s[n-1-char]:
                return False 
        return True 



        