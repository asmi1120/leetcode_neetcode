class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if self.eat(piles,h,mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
    def eat(self,piles,h,mid):
        hr=0
        for i in piles:
            hr+=(i+mid-1)//mid
        return hr<=h
        