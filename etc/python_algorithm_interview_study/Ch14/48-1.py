# https://leetcode.com/problems/balanced-binary-tree/
# 72ms 18.5MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isBalanced(root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)

            # 높이 차이가 1이상 난경우 계속 -1 리턴
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        # -1이면 균형 이진트리 아니다.
        return check(root) != -1