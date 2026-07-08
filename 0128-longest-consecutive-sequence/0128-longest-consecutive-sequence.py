class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        count=0
        for r in range(len(nums)):
            if r>0:
                if nums[r] - nums[r-1] > 1:
                    l = r  
                elif nums[r] == nums[r-1]:
                    l += 1
            count=max(count,r-l+1)
        return count