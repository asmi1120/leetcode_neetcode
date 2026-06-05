class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=1
        r=x//2
        while l<=r:
            mid= (l+r)//2
            s=mid*mid
            if s==x:
                return mid
            if s<x:
                l=mid+1
            else:
                r=mid-1
        return r
        
        