class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans=[]
        def solve(i,curr):
            if i==len(digits):
                ans.append(curr)
                return
            for c in d[digits[i]]:
                solve(i+1,curr+c)

        solve(0,"")
        return ans
        