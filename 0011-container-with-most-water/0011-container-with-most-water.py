class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=0
        while i<j:
            if height[i]<height[j]:
                h=height[i]
                area=max(area,h*(j-i))
                i+=1
            else:
                h=height[j]
                area=max(area,h*(j-i))
                j-=1
            
        return area
        