# https://leetcode.com/problems/range-sum-of-bst/
# 399ms 22.9MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
        result = 0

        def inorder(root):
            nonlocal result
            if root:
                inorder(root.right)
                if low <= root.val <= high:
                    result = result + root.val
                inorder(root.left)

        inorder(root)
        return result
