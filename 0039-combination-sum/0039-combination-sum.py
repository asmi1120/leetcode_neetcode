class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        candidates.sort()
        def b(s,path,remain):
            if remain==0:
                r.append(path[:])
                return
            for i in range(s,len(candidates)):
                if candidates[i]>remain:
                    break
                path.append(candidates[i])
                b(i,path,remain-candidates[i])
                path.pop()
        b(0,[],target)
        return r
        