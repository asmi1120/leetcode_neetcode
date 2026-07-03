class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r=[]
        def b(s,path):
            if len(path)>len(nums):
                return
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                if len(path)==len(nums):
                    r.append(path[:])
                b(i+1,path)
                path.pop()
        b(0,[])
        return r