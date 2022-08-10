# https://leetcode.com/problems/merge-two-binary-trees/
# 107ms 15.4MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 두개의 노드가 모두 있는 경우
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.right = self.mergeTrees(root1.right, root2.right)
            node.left = self.mergeTrees(root1.left, root2.left)
            return node
        # 하나 빈경우
        else:
            return root1 or root2
