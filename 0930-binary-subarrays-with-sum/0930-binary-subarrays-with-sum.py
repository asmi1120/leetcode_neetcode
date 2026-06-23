class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.at(goal,nums)-self.at(goal-1,nums)
    def at(self,goal,nums):
        if goal < 0:
            return 0
        count=0
        l=0
        sumt=0
        for r in range(len(nums)):
            sumt+=nums[r]
            while sumt>goal:
                sumt-=nums[l]
                l+=1
            count+=(r-l+1)
        return count
