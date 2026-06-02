class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        L, R, p = 0, n-1, n-1
        while L <= R:
            lSq, rSq = nums[L]**2, nums[R]**2
            if lSq > rSq: ans[p] = lSq; L += 1
            else:  ans[p] = rSq; R -= 1
            p -= 1
        return ans