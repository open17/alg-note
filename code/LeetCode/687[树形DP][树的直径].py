# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans=0
        def f(root):
            if not root:
                return 0
            l=f(root.left)
            r=f(root.right)
            if not l or root.left.val!=root.val: l=0
            if not r or root.right.val!=root.val: r=0
            nonlocal ans
            ans=max(ans,l+r+1)
            return max(l,r)+1
        f(root)
        return max(ans-1,0)
            
