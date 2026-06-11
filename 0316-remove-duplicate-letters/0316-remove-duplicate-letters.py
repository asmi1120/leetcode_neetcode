class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l={char:i for i,char in enumerate(s)}
        st=[]
        sp=set()
        for i,m in enumerate(s):
            if m in sp:
                continue
            while st and m<st[-1] and i<l[st[-1]]:
                val=st.pop()
                sp.remove(val)
            st.append(m)
            sp.add(m)
        return "".join(st)
        