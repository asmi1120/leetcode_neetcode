class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        l=1
        r=sum(candies)//k
        ans=1
        while l<=r:
            mid=(l+r)//2
            count=0
            for i in candies:
                if i>=mid:
                    count+=i//mid
                if count>=k:
                    break
            if count>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
   
                