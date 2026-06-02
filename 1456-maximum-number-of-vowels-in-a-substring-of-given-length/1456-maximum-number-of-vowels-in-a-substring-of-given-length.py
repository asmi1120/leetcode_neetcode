class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v={'a','e','i','o','u'}
        c_v=sum(1 for i in range(k) if s[i] in v)
        max1=c_v
        for i in range(k,len(s)):
            if s[i] in v:
                c_v+=1
            if s[i-k] in v:
                c_v-=1
            max1=max(max1,c_v)
            if max1==k:
                return k
        return max1