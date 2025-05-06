"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        ans = 0
        while q:
            l = len(q)
            ans += 1
            for i in range(l):
                cur = q.popleft()
                for nei in cur.children:
                    q.append(nei)
        
        return ans