class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while k>0 and st and i<st[-1]:
                st.pop()
                k-=1
            st.append(i)
        st=st[:len(st)-k]
        s=0
        while s<len(st) and st[s]=='0':
            s+=1
        a="".join(st[s:])
        return a if a else "0"
