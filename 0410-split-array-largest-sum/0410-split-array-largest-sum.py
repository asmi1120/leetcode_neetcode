class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if self.ss(nums,k,mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
    def ss(self,nums,k,mid):
        grp=1
        sump=0
        for i in nums:
            if sump+i<=mid:
                sump+=i
            else:
                grp+=1
                sump=i
        return grp<=k

        