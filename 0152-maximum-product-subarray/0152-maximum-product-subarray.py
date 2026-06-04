class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        max_pro=float('-inf')
        for r in range(len(nums)):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix*=nums[r]
            suffix*=nums[len(nums)-r-1]
            max_pro=max(max_pro,max(prefix,suffix))
            
        return max_pro
