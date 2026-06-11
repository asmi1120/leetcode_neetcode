class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d=0
        st=0
        for i in range(len(s)):
            if s[i] == '(':
                d+=1
            else:
                d-=1
                if s[i-1] == '(':
                    st+=1<<d
        return st