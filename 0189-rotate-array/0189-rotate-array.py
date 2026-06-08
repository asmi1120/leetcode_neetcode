class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[0]*len(nums)
        k=k%len(nums)
        for i in range(len(nums)):
            s=(i+k)%len(nums)
            temp[s]=nums[i]
        for i in range(len(nums)):
            nums[i]=temp[i]
        