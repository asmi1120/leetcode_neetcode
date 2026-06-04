class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        answer.insert(0,1)
        for r in range(1,len(nums)):
            answer.insert(r,answer[r-1]*nums[r-1])
        right=1
        for j in range(len(nums)-1,-1,-1):
            answer[j]=answer[j]*right
            right=right*nums[j]   
        return answer

