class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in s:
            if st and abs(ord(st[-1])-ord(i))==32:
                st.pop()
            else:
                st.append(i)
        return "".join(st)
        