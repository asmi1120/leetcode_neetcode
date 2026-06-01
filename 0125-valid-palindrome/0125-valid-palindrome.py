class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        c="".join([char for char in s if char.isalnum()])
        i=0
        j=len(c)-1
        while i<j:
            if c[i]!=c[j]:
                return False
            i+=1
            j-=1           
        return True
