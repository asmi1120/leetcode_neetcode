class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
            
        n = len(heights)
        less_from_left = [0] * n   # Stores first shorter index to the left
        less_from_right = [0] * n  # Stores first shorter index to the right
        
        # 1. Populate less_from_left using pointer jumping
        less_from_left[0] = -1
        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]  # Jump over taller bars
            less_from_left[i] = p

        # 2. Populate less_from_right using pointer jumping
        less_from_right[n - 1] = n
        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = less_from_right[p]  # Jump over taller bars
            less_from_right[i] = p

        # 3. Calculate max area for each bar
        max_area = 0
        for i in range(n):
            width = less_from_right[i] - less_from_left[i] - 1
            max_area = max(max_area, heights[i] * width)
            
        return max_area

        