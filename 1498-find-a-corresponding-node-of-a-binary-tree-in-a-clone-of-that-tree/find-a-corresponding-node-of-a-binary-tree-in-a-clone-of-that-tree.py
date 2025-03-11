# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def travel(original, cloned):
            if not original and not cloned:
                return None
            if original == target:
                return cloned
            
            return travel(original.left, cloned.left) or travel(original.right, cloned.right)
        return travel(original, cloned)