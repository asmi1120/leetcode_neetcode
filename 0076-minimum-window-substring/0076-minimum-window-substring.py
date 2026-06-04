class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""
        T,sw={},{}
        for i in range(len(t)):
            T[t[i]]=1+T.get(t[i],0)
        ans=[0,0]
        ansmin=float('inf')
        have,need=0,len(T)
        l=0
        for r in range(len(s)):
            m=s[r]
            sw[m]=1+sw.get(m,0)
            if m in T and sw[m] == T[m]:
                have+=1
            while have == need :
                if r-l+1 < ansmin:
                    ans=[l,r]
                    ansmin=r-l+1
                c=s[l]
                sw[c]-=1
                if c in T and sw[c] < T[c]:
                    have-=1
                l+=1
        if ansmin == float('inf'):
            return ""
        l,r=ans
        return s[l:r+1]






