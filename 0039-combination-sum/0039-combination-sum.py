class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        def b(s,path):
            if sum(path)>=target: return
            for i in range(s,len(candidates)):
                path.append(candidates[i])
                if sum(path)==target:
                    r.append(path[:])
                b(i,path)
                path.pop()
        b(0,[])
        return r
        