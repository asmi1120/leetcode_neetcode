class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st : return False
                elif i in ")" and st[-1]!="(": return False
                elif i in "}" and st[-1]!="{": return False
                elif i in "]" and st[-1]!="[": return False
                st.pop()
        return not st
        