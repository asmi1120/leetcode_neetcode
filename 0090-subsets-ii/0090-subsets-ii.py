class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r=[[]]
        def b(s,path):
            if len(path)==len(nums): return
            for i in range(s,len(nums)):
                if i > s and nums[i] == nums[i-1]: 
                    continue
                path.append(nums[i])
                r.append(path[:])
                b(i+1,path)
                path.pop()
        b(0,[])
        return r