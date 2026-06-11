class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        c=0
        for i,ch in enumerate(s):
            if ch in "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ci=i-st[-1]
                    c=max(c,ci)
        return c
        