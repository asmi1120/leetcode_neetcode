class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.b(s) == self.b(t)
    def b(self,s):
        st=[]
        for i in s:
            if i in "#" and st:
                st.pop()
            elif i != "#":
                st.append(i)
        return "".join(st)


            
        