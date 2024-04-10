# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def f(root):
            if not root:
                return -1
            l=f(root.left)
            r=f(root.right)
            nonlocal ans
            ans=max(ans,l+r+2)

            return max(l,r)+1
        f(root)
        return ans