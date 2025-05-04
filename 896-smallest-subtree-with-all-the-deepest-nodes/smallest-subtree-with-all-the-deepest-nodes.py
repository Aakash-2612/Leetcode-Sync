# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, depth):
            if not node:
                return (None, depth)

            left_node, left_depth = helper(node.left, depth + 1)
            right_node, right_depth = helper(node.right, depth+1)

            if left_depth > right_depth:
                return (left_node, left_depth)
            elif left_depth < right_depth:
                return (right_node, right_depth)
            else:
                return (node, left_depth)
        
        lca_node, _ = helper(root, 0)
        return lca_node