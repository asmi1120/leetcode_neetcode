class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        c=0
        for i in s:
            if i in "(":
                st.append(0)
            else:
                val=st.pop()
                c=(max(2*val,1))
                st.append(c+st.pop())
        return st.pop()        