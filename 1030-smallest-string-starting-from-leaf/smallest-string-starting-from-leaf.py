# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        alp = [chr(i) for i in range(97, 123)]
        temp = []
        def preorder(root, temp):
            if not root:
                return
            if not root.left and not root.right:
                temp.append(root.val)
                ans.append("".join([alp[i] for i in reversed(temp)]))
                temp.pop()
                return
            
            temp.append(root.val)
            preorder(root.left, temp)
            preorder(root.right, temp)
            temp.pop()
        preorder(root, temp)
        print(ans)
        return min(ans)
        
        