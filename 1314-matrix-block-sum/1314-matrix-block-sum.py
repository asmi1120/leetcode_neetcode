class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        prefix=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix[i][j]=mat[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]
        ans=[[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                r1=max(0,i-k)
                c1=max(0,j-k)
                r2=min(m-1,i+k)
                c2=min(n-1,j+k)
                r1+=1
                c1+=1
                r2+=1
                c2+=1
                ans[i][j]=prefix[r2][c2]-prefix[r1-1][c2]-prefix[r2][c1-1]+prefix[r1-1][c1-1]
        return ans


