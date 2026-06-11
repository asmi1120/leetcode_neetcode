class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening=0
        close=0
        for i in s:
            if i in "(":
                opening+=1
            else:
                if opening>0:
                    opening-=1
                else:
                    close+=1
        return opening+close