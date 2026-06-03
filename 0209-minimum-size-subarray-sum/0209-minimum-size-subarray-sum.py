class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       sums=0
       ans=float('inf')
       l=0
       for r in range(len(nums)):
        sums+=nums[r]
        while(sums>=target):
            ans=min(ans,r-l+1)
            sums-=nums[l]
            l+=1
       if ans == inf:
        return 0
       return ans



        