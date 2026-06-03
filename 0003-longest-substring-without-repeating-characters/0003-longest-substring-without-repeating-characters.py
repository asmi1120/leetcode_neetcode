class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sw=set()
        ans=0
        l=0
        for r in range(len(s)):
            while s[r] in sw:
                sw.remove(s[l])
                l+=1
            sw.add(s[r])
            ans=max(ans,r-l+1)
        return ans