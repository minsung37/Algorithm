# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 39ms 14MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val = self.val + root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root
