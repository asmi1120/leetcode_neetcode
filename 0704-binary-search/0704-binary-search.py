class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.check(nums,0,len(nums)-1,target)

    
    def check(self,nums,l,r,target):
        mid=(l+r)//2
        if l>r:
            return -1
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            return self.check(nums,l,mid-1,target)
        else:
            return self.check(nums,mid+1,r,target)


        