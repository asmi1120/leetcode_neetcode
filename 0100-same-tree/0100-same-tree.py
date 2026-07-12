# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(np,nq):
            if np is None and nq is None:
                return True
            if np is None or nq is None:
                return False
            if np.val!=nq.val:
                return False
            return dfs(np.left,nq.left) and dfs(np.right,nq.right)
        return dfs(p,q)