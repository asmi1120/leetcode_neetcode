class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        hp={n:i for i,n in enumerate(nums)}
        res = [-1] * len(nums)
        stack = [] 
        for i in range(2*len(nums),-1,-1):
            cur=nums[i%len(nums)]
            while stack and stack[-1]<=cur:
                stack.pop()
            if i<len(nums) and stack:
                res[i] = stack[-1] 
            stack.append(cur)  
        return res
            