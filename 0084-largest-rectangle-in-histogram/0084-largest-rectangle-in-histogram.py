class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(0,len(heights)+1):
            hi = 0 if (i==len(heights)) else heights[i]
            while stack and hi<heights[stack[-1]]:
                h=heights[stack.pop()]
                width= i if (len(stack)==0) else i-stack[-1]-1
                max_area=max(max_area,h*width)
            stack.append(i)
        return max_area
        