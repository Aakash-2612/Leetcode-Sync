# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root, res):
            if not root:
                return 0
            l = helper(root.left, res)
            r = helper(root.right, res)
            res[0] = max(res[0], l + r)

            return max(l, r) + 1
        res = [0]
        helper(root, res)
        return res[0]
