# https://leetcode.com/problems/longest-univalue-path/
# 838ms	18.1MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(5)
root.right = right
root.left = left

left1 = TreeNode(1)
right1 = TreeNode(1)
left.left = left1
left.right = right1

left2 = TreeNode(None)
right2 = TreeNode(5)
right.left = left2
right.right = right2


class Solution:
    @staticmethod
    def longestUnivaluePath(root: TreeNode) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left = left + 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right = right + 1
            else:
                right = 0
            result = max(result, left + right)
            print(left, right)
            return max(left, right)

        dfs(root)
        return result


Solution.longestUnivaluePath(root)