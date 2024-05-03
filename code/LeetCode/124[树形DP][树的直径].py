# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-inf
        def f(root):
            if not root:
                return 0
            l=f(root.left)
            r=f(root.right)
            nonlocal ans
            ans=max(ans,l+r+root.val)
            return max(0,l+root.val,r+root.val)
        f(root)
        return ans