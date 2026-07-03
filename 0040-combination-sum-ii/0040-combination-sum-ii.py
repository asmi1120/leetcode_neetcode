class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        candidates.sort()
        def b(s,path):
            if sum(path)>=target: return
            for i in range(s,len(candidates)):
                if i > s and candidates[i] == candidates[i-1]: 
                    continue
                path.append(candidates[i])
                if sum(path)==target:
                    r.append(path[:])
                b(i+1,path)
                path.pop()
        b(0,[])
        return r