class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        i=0
        j=len(nums)-1
        p=len(nums)-1
        while i<=j:
            l=nums[i]**2
            r=nums[j]**2
            if l>r:
                arr[p]=l
                i+=1
            else:
                arr[p]=r
                j-=1
            p-=1
        return arr
