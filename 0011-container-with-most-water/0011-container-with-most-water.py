class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        area=0
        r=len(height)-1
        while l<=r:
            if height[l]>height[r]:
                h=height[r]
                r-=1
            else:
                h=height[l]
                l+=1
            area=max(area,h*(r-l+1))
        return area

        

        