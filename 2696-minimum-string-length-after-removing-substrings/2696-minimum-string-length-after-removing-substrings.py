class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for i in s:
            if st:
                if (st[-1]=="A" and i =="B") or (st[-1]=="C" and i =="D"):
                    st.pop()
                    continue
            st.append(i)
        return len(st)