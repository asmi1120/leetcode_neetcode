class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        r=[]
        path=[]
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        def b():
            if len(path)==len(nums):
                r.append(path[:])
                return
            for n in count:
                if count[n]>0:
                    path.append(n)
                    count[n]-=1
                    b()
                    count[n]+=1
                    path.pop()
        b()
        return r
        