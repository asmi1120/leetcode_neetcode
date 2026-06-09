class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if self.cap(weights,days,mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
    def cap(self,weights,days,mid):
        d=1
        sumt=0
        for w in weights:
            sumt+=w
            if sumt>mid:
                d+=1
                sumt=w
        return d<=days
        