class Solution:
    def myPow(self, x: float, n: int) -> float:
        e=n
        if e<0:
            x=1/x
            e=-e
        return self.pow1(x,e,1)
    def pow1(self,x,n,ans):
        if n==0:
            return ans
        if n%2==1:
            ans=ans*x
        return self.pow1(x*x,n//2,ans)