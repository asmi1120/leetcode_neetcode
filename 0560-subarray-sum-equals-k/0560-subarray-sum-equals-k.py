class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        mp={0:1}
        count=0
        for i in nums:
            prefix+=i
            if prefix-k in mp:
                count+=mp[prefix-k]
            mp[prefix]=1+mp.get(prefix,0)
        return count