# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None
        def travel(original, cloned):
            if not original and not cloned:
                return None
            if original == target:
                self.ans = cloned
                return
            
            travel(original.left, cloned.left)
            travel(original.right, cloned.right)

        travel(original, cloned)
        return self.ans