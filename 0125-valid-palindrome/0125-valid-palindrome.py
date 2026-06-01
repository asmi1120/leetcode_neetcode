class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        c="".join([char for char in s if char.isalnum()])
        m=c[::-1]
        if c==m:
            return True
        else:
            return False
        