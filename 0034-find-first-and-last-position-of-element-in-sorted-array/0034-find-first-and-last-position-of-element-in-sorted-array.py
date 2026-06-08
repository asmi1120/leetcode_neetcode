class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.FF(nums,target),self.FL(nums,target)]
    def FF(self,nums,target):
        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]==target:
                ans=mid
                r=mid-1
            else:
                r=mid-1
        return ans

    def FL(self,nums,target):
        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]==target:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
    
        