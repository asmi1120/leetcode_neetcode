class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        ans = list(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if st:
                    st.pop()  
                else:
                    ans[i] = "" 
        for i in st:
            ans[i] = ""
            
        return "".join(ans)
            
        


        