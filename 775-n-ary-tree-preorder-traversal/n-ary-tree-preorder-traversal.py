"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def helper(root):
            if not root:
                return
            
            arr.append(root.val)
            for i in root.children:
                helper(i)
        
        helper(root)
        return arr
