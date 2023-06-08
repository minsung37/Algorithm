# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 35ms 14MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def bstToGst(root: TreeNode) -> TreeNode:
        result = 0

        def inorder(root):
            nonlocal result
            if root:
                inorder(root.right)
                root.val = root.val + result
                result = root.val
                inorder(root.left)
        inorder(root)
        return root