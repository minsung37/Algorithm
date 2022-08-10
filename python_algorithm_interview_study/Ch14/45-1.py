# https://leetcode.com/problems/invert-binary-tree/
# 34ms 13.8MB
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])
        while q:
            x = q.popleft()
            if x:
                x.right, x.left = x.left, x.right
                q.append(x.right)
                q.append(x.left)
        return root