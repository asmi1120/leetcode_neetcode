class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[]
        def b(s,path):
            r.append(path[:])
            for i in range(s,len(nums)):
                path.append(nums[i])
                b(i+1,path)
                path.pop()
        b(0,[])
        return r   


