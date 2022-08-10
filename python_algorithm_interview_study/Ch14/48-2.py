# https://leetcode.com/problems/balanced-binary-tree/
# 91ms 19.2MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isBalanced(root: TreeNode) -> bool:
        tree = []

        def tree_depth(root, depth) -> int:
            if not root:
                tree.append(depth)
                return 0
            right = tree_depth(root.right, depth + 1)
            left = tree_depth(root.left, depth + 1)
            if abs(right - left) > 1:
                tree.append(-1)
            return max(right, left) + 1
        tree_depth(root, 0)
        if -1 in tree:
            return False
        else:
            return True